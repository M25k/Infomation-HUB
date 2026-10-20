"""cad2rt/shots.py – Review-Renders. Aufruf:
blender -b MASTER.blend --python shots.py -- OUTDIR PREFIX [cams.json]   (ohne cams.json: Kameras aus Gruppen berechnen und speichern)
Modi über env SHOTS=gesamt,wire,detail,uv"""
import bpy,sys,json,math,os
from mathutils import Vector
a=sys.argv[sys.argv.index("--")+1:]; OUTD=a[0]; PRE=a[1]; CJ=a[2] if len(a)>2 else None
os.makedirs(OUTD,exist_ok=True); sc=bpy.context.scene
modes=os.environ.get("SHOTS","gesamt,wire,detail").split(",")
for c in bpy.data.collections: pass
w=bpy.data.worlds.new("w"); sc.world=w; w.use_nodes=True; bg=w.node_tree.nodes["Background"]; bg.inputs[0].default_value=(0.6,0.62,0.66,1); bg.inputs[1].default_value=0.8
for n,rot,e in [("key",(50,0,40),4),("fill",(60,0,-130),1.5),("rim",(-40,0,180),3)]:
    ld=bpy.data.lights.new(n,'SUN'); ld.energy=e; lo=bpy.data.objects.new(n,ld); sc.collection.objects.link(lo); lo.rotation_euler=[math.radians(x) for x in rot]
cd=bpy.data.cameras.new("cam"); cam=bpy.data.objects.new("cam",cd); sc.collection.objects.link(cam); sc.camera=cam; cd.lens=60; cd.clip_start=0.005
sc.render.resolution_x=1600; sc.render.resolution_y=1200; sc.render.engine='BLENDER_EEVEE'
for lc in bpy.context.view_layer.layer_collection.children: lc.hide_viewport=False; lc.exclude=False
meshes=[o for o in sc.objects if o.type=='MESH']
def lod(o):
    for c in o.users_collection:
        if c.name.startswith("LOD"): return int(c.name[3])
    import re
    m=re.search(r"_LOD(\d)",o.name)
    return int(m.group(1)) if m else -1
def show(objs):
    for o in meshes: o.hide_render=o not in objs
def look(t,dist,az,el):
    t=Vector(t); d=Vector((math.cos(math.radians(el))*math.sin(math.radians(az)),-math.cos(math.radians(el))*math.cos(math.radians(az)),math.sin(math.radians(el))))
    cam.location=t+d*dist; cam.rotation_euler=(-d).to_track_quat('-Z','Y').to_euler()
def shot(n): sc.render.filepath=f"{OUTD}/{PRE}{n}.png"; bpy.ops.render.render(write_still=True)
def bbc(objs):
    vs=[o.matrix_world@Vector(c) for o in objs for c in o.bound_box]
    return [(min(v[i] for v in vs)+max(v[i] for v in vs))/2 for i in range(3)]
L0=[o for o in meshes if lod(o)==0]
if CJ and os.path.exists(CJ): cams=json.load(open(CJ))
else:
    g=lambda s:[o for o in L0 if s in o.name]
    cams={"gesamt":[bbc(L0),0.75,-60,20],"gesamt_hinten":[bbc(L0),0.75,120,15],
          "detail_Rohr":[bbc(g("Rohrkoerper")),0.22,-35,10],"detail_Kupplung":[bbc(g("StorzC")),0.22,150,20],
          "detail_Hebel":[bbc(g("Hebel")),0.30,-70,35]}
    if CJ: json.dump(cams,open(CJ,"w"))
if "gesamt" in modes or "detail" in modes:
    show(L0)
    for k,v in cams.items():
        if (k.startswith("detail") and "detail" in modes) or (k.startswith("gesamt") and "gesamt" in modes): look(*v); shot(k)
if "wire" in modes:
    wm=bpy.data.materials.new("wire"); wm.use_nodes=True; wm.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value=(0,0,0,1)
    gm=bpy.data.materials.new("grey"); gm.use_nodes=True; gm.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value=(0.7,0.7,0.7,1)
    for i in sorted({lod(o) for o in meshes}):
        objs=[o for o in meshes if lod(o)==i]; show([]); tmp=[]
        for o in objs:
            g_=o.copy(); g_.data=o.data.copy(); g_.data.materials.clear(); g_.data.materials.append(gm)
            w_=o.copy(); w_.data=o.data.copy(); w_.data.materials.clear(); w_.data.materials.append(wm)
            m=w_.modifiers.new("w",'WIREFRAME'); m.thickness=0.00025; m.use_replace=True
            for x in (g_,w_): sc.collection.objects.link(x); x.hide_render=False; tmp.append(x)
        tr=sum(sum(len(p.vertices)-2 for p in o.data.polygons) for o in objs)
        look(*cams["gesamt"]); shot(f"wireframe_LOD{i}_{tr}tris")
        if i==0:
            for k in ("detail_Rohr","detail_Kupplung","detail_Hebel"): look(*cams[k]); shot(f"wireframe_LOD0_{k}")
        for x in tmp: bpy.data.objects.remove(x)
