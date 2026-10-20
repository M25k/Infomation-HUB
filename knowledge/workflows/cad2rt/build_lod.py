"""cad2rt/build_lod.py – baut EIN LOD (Lowpoly, Seams, UV, Bake gegen CAD-Highpoly, Teile/Pivots).
Aufruf: blender -b --python build_lod.py -- CONFIG.json LOD_INDEX
Voraussetzung: tess.py hat WORK/HIGH.obj (+ --normals) und WORK/L{i}.obj + _edges.json erzeugt."""
import bpy, bmesh, sys, json, math, os, re, time
import numpy as np
from mathutils import Vector, Matrix, kdtree
argv=sys.argv[sys.argv.index("--")+1:]; cfg=json.load(open(argv[0])); LI=int(argv[1])
L=cfg["lods"][LI]; TEX=L["tex"]; W=cfg["work"]; OUT=cfg["out"]; NM=cfg["name"]
PAD=cfg.get("padding_px",16); SHARP=math.radians(cfg.get("sharp_angle_deg",30))
os.makedirs(OUT+"/textures",exist_ok=True)
t0=time.time(); log=lambda *a: print(f"[{time.time()-t0:6.1f}s]",*a,flush=True)
bpy.ops.wm.read_factory_settings(use_empty=True); sc=bpy.context.scene
sc.unit_settings.system='METRIC'; sc.unit_settings.scale_length=1.0
def imp(path,prefix):
    before=set(bpy.data.objects); bpy.ops.wm.obj_import(filepath=path,forward_axis='Y',up_axis='Z')
    objs=[o for o in bpy.data.objects if o not in before]
    for o in objs: o.name=prefix+re.sub(r"\.\d{3}$","",o.name)
    return {o.name[len(prefix):]:o for o in objs}
H=imp(W+"/HIGH.obj","H_"); log("high",len(H))
Lo=imp(W+f"/L{LI}.obj","L_"); log("low",len(Lo))
keys=[k for k in Lo if k in H]
if L.get("drop"): keys=[k for k in keys if not any(d in k for d in cfg.get("lod_drop",[]))]
# ---- Transform: Pivot = BBox-Mitte origin_part, Drehung um X
op=[k for k in keys if cfg["origin_part"] in k][0]
bb=[Vector(c) for c in H[op].bound_box]
piv=Vector([(min(v[i] for v in bb)+max(v[i] for v in bb))/2 for i in range(3)])
T=Matrix.Rotation(math.radians(cfg.get("rotate_x_deg",0)),4,'X')@Matrix.Translation(-piv)
for o in list(H.values())+list(Lo.values()): o.data.transform(T); o.data.update()
axis0=T@Vector((0,0,0))  # Punkt auf Rohrachse (CAD-Achse = Z durch 0,0)
# ---- Materialien (Quelle, flache PBR-Werte)
def matcat(n):
    for k,v in cfg["materials"].items():
        if any(s in n for s in v["match"]): return k
    return [k for k,v in cfg["materials"].items() if not v["match"]][0]
SRC={}
for k,v in cfg["materials"].items():
    M=bpy.data.materials.new("SRC_"+k); M.use_nodes=True; SRC[k]=M
for k in keys:
    for o in (H[k],Lo[k]): o.data.materials.clear(); o.data.materials.append(SRC[matcat(k)])
for o in H.values():
    for p in o.data.polygons: p.use_smooth=True
DEC={}  # Materialname -> (Kategorie, Decal-Config, Teil)
for di,dc in enumerate(cfg.get("decals",[])):
    for k in keys:
        if dc["match"] in k:
            cat=matcat(k); M=SRC[cat].copy(); M.name=f"SRC_{cat}_DEC{di}"; DEC[M.name]=(cat,dc,k)
            Lo[k].data.materials.clear(); Lo[k].data.materials.append(M)
# ---- Lowpoly: Merge, Seams aus CAD-Kanten, Planar-Dissolve, Decimate mit Schutz
def tris(o): return sum(len(p.vertices)-2 for p in o.data.polygons)
def grp(k):
    for g in cfg["groups"]:
        if any(s in k for s in g["match"]): return g
ROUND={k for k in keys if grp(k)["pivot"]=="barrel_axis"}
def prep(k):
    o=Lo[k]; bm=bmesh.new(); bm.from_mesh(o.data)
    bmesh.ops.remove_doubles(bm,verts=bm.verts,dist=2e-6)
    multi=sum(1 for e in bm.edges if len(e.link_faces)>2)
    if multi>max(50,0.005*len(bm.edges)):
        bm.to_mesh(o.data); bm.free()
        vs=L.get("voxel_mm",max(0.35,L["lin"]*1.5))/1000
        rm=o.modifiers.new("v",'REMESH'); rm.mode='VOXEL'; rm.voxel_size=vs
        bpy.context.view_layer.objects.active=o; bpy.ops.object.modifier_apply(modifier="v")
        log("VOXEL-Remesh (nicht-manifold CAD)",k,multi,"->",tris(o),"voxel",vs)
        bm=bmesh.new(); bm.from_mesh(o.data)
    for e in bm.edges:
        if e.is_manifold and e.calc_face_angle(0.0)>SHARP: e.smooth=False
    bmesh.ops.dissolve_limit(bm,angle_limit=math.radians(0.5),verts=bm.verts,edges=bm.edges,delimit={'SHARP','MATERIAL'})
    bmesh.ops.triangulate(bm,faces=bm.faces,quad_method='BEAUTY',ngon_method='BEAUTY')
    for f in bm.faces: f.smooth=True
    bm.to_mesh(o.data); bm.free()
for k in keys: prep(k)
CULL=cfg.get("cull_hidden")
if CULL:
    from mathutils.bvhtree import BVHTree
    allbm=bmesh.new()
    for k in keys: allbm.from_mesh(Lo[k].data)
    bvh=BVHTree.FromBMesh(allbm); allbm.free()
    nd=CULL.get("rays",64); ga=math.pi*(3-math.sqrt(5))
    DIRS=[Vector((math.cos(ga*i)*math.sqrt(1-(1-2*(i+.5)/nd)**2),math.sin(ga*i)*math.sqrt(1-(1-2*(i+.5)/nd)**2),1-2*(i+.5)/nd)) for i in range(nd)]
    thr=CULL.get("min_visible",0.03); removed=0; before=0
    for k in keys:
        o=Lo[k]; bm=bmesh.new(); bm.from_mesh(o.data); bm.faces.ensure_lookup_table(); dead=[]
        for f in bm.faces:
            c=f.calc_center_median(); n=f.normal; tot=esc=0
            # Mittelpunkt + Eckpunkte (leicht nach innen) testen: sichtbar, wenn irgendein Punkt genug freie Strahlen hat
            pts=[c]+[v.co.lerp(c,0.3) for v in list(f.verts)[:CULL.get('extra_pts',1)]]
            vis=False
            for p in pts:
                p=p+n*2e-5; tot=esc=0; need=max(1,int(thr*nd/2))
                for d in DIRS:
                    if d.dot(n)<=0.02: continue
                    tot+=1
                    if bvh.ray_cast(p,d,1.0)[0] is None:
                        esc+=1
                        if esc>=need: break
                if esc>=need: vis=True; break
            if not vis: dead.append(f)
        before+=len(bm.faces); removed+=len(dead)
        bmesh.ops.delete(bm,geom=dead,context='FACES'); bmesh.ops.delete(bm,geom=[v for v in bm.verts if not v.link_faces],context='VERTS'); bm.to_mesh(o.data); bm.free()
    log("Verdeckte Flächen entfernt",removed,"von",before)
pre=sum(tris(Lo[k]) for k in keys); log("nach dissolve",pre)
A={k:sum(f.area for f in Lo[k].data.polygons) for k in keys}; At=sum(A.values()); Tt=pre
target=L["tris"]; r=target/pre
RB=cfg.get("round_budget_boost",1.5)
def BB(k):
    for s_,f_ in cfg.get("budget_boost",{}).items():
        if s_ in k: return f_
    return 1.0
def want(k,r): return min(tris(Lo[k]),max((0.6*A[k]/At+0.4*tris(Lo[k])/Tt)*pre*r*(RB if k in ROUND else 1)*BB(k),24))
for it in range(10):
    tot=0
    for k in keys:
        o=Lo[k]; o.modifiers.clear(); m=o.modifiers.new("d",'DECIMATE'); m.ratio=min(1,want(k,r)/max(1,tris(o))); m.use_collapse_triangulate=True
    dg=bpy.context.evaluated_depsgraph_get()
    for k in keys: tot+=len(Lo[k].evaluated_get(dg).data.polygons)
    log("iter",it,round(r,4),tot)
    if abs(tot-target)/target<0.04: break
    r*=target/tot
AX=Vector((0,1,0)); HID=Vector(cfg.get("hidden_dir",[0,0,-1]))
HARD=math.radians(cfg.get("hard_angle_deg",60)); CONE=math.cos(math.radians(cfg.get("chart_cone_deg",50)))
def seams(k):
    """Chart-Segmentierung: Region-Growing (Normalen-Kegel), harte Kanten = Seam+Sharp,
    Rotationsteile: Mantel als ein Streifen, Schnitt entlang verdeckter Linie (hidden_dir)."""
    o=Lo[k]; bm=bmesh.new(); bm.from_mesh(o.data); bm.faces.ensure_lookup_table()
    hard=set()
    for e in bm.edges:
        e.seam=False; e.smooth=True
        if not e.is_manifold or e.calc_face_angle(0.0)>HARD: hard.add(e); e.smooth=False
    rnd=k in ROUND; ref=HID; side=AX.cross(ref)
    def kind(f):
        if not rnd: return "f"
        d=f.normal.dot(AX)
        return "c+" if d>0.7 else ("c-" if d<-0.7 else "r")
    def phi(f):
        c=f.calc_center_median()-axis0; c=c-AX*c.dot(AX); return math.atan2(c.dot(side),c.dot(ref))
    K={f:kind(f) for f in bm.faces}; PH={f:phi(f) for f in bm.faces if K[f]=="r"}
    ch={}; cid=0
    for seed in sorted(bm.faces,key=lambda f:-f.calc_area()):
        if seed in ch: continue
        ch[seed]=cid; N=seed.normal*seed.calc_area(); st=[seed]
        while st:
            f=st.pop()
            for e in f.edges:
                if e in hard: continue
                for g in e.link_faces:
                    if g in ch or K[g]!=K[seed]: continue
                    if K[g]=="r":
                        if abs(PH[f])<1.2 and abs(PH[g])<1.2 and (PH[f]>=0)!=(PH[g]>=0): continue
                    elif g.normal.dot(N.normalized())<CONE: continue
                    ch[g]=cid; N+=g.normal*g.calc_area(); st.append(g)
        cid+=1
    # Mini-Charts (<MINF Flächen) in Nachbar-Chart mit längster gemeinsamer Kante mischen
    MINF=cfg.get("min_chart_faces",6)
    for it_ in range(6):
        allow_hard=it_>=3
        cnt={}
        for f,c in ch.items(): cnt[c]=cnt.get(c,0)+1
        changed=0
        for f in bm.faces:
            c=ch[f]
            if cnt[c]>=MINF: continue
            best={}
            for e in f.edges:
                if e in hard and not (allow_hard and e.is_manifold): continue
                for g in e.link_faces:
                    if ch[g]!=c: best[ch[g]]=best.get(ch[g],0)+e.calc_length()
            if best:
                n=max(best,key=best.get); cnt[c]-=1; cnt[n]=cnt.get(n,0)+1; ch[f]=n; changed+=1
        if not changed and allow_hard: break
    for e in bm.edges:
        lf=e.link_faces
        if not e.is_manifold or len(lf)!=2 or ch[lf[0]]!=ch[lf[1]]: e.seam=True
    o["charts"]=len(set(ch.values())); log("charts",k[:30],o["charts"],len(bm.faces),"hard",len(hard))
    bm.to_mesh(o.data); bm.free()
for k in keys:
    o=Lo[k]; bpy.context.view_layer.objects.active=o; bpy.ops.object.modifier_apply(modifier="d")
for k in keys:
    o=Lo[k]; bpy.context.view_layer.objects.active=o
    seams(k)
    wn=o.modifiers.new("wn",'WEIGHTED_NORMAL'); wn.keep_sharp=True; wn.mode='FACE_AREA'; bpy.ops.object.modifier_apply(modifier="wn")
for k in keys:
    for s_,mm in cfg.get("offset_mm",{}).items():
        if s_ in k:
            me=Lo[k].data
            for v in me.vertices: v.co+=v.normal*(mm/1000)
            log("Offset",k[:30],mm,"mm (Z-Fighting)")
lows=[Lo[k] for k in keys]
log("LOW tris",sum(tris(o) for o in lows),"charts",sum(o["charts"] for o in lows),"seams",sum(sum(1 for e in o.data.edges if e.use_seam) for o in lows))
# ---- UV: Unwrap an Seams, Texeldichte angleichen, packen
for o in sc.objects: o.select_set(False)
for o in lows: o.select_set(True)
bpy.context.view_layer.objects.active=lows[0]
bpy.ops.object.mode_set(mode='EDIT'); bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.uv.unwrap(method='ANGLE_BASED',fill_holes=True,correct_aspect=True,margin=0.0)
bpy.ops.object.mode_set(mode='OBJECT')
def pack_uniform(objs,pad_uv):
    """Eigener Packer: einheitliche Texeldichte (UV-Fläche ~ 3D-Fläche), PCA-Rotation, Shelf-Packing, Padding garantiert."""
    isl=[]  # (bm, uvlayer, faces)
    bms=[]
    for o in objs:
        bm=bmesh.new(); bm.from_mesh(o.data); uvl=bm.loops.layers.uv.active; bms.append((o,bm))
        boost=1.0
        for s_,f_ in cfg.get("texel_boost",{}).items():
            if s_ in o.name: boost=f_
        seen=set()
        for f in bm.faces:
            if f.index in seen: continue
            st=[f]; seen.add(f.index); fs=[]
            while st:
                g=st.pop(); fs.append(g)
                for e in g.edges:
                    if e.seam: continue
                    for h in e.link_faces:
                        if h.index not in seen: seen.add(h.index); st.append(h)
            isl.append((uvl,fs,boost))
    rects=[]
    for uvl,fs,boost in isl:
        loops=[l for f in fs for l in f.loops]
        P=np.array([l[uvl].uv[:] for l in loops]); a3=sum(f.calc_area() for f in fs)
        ua=0.0
        for f in fs:
            q=[l[uvl].uv for l in f.loops]
            for i in range(1,len(q)-1): ua+=abs((q[i]-q[0]).cross(q[i+1]-q[0]))/2
        if ua<1e-12 or not np.isfinite(P).all():  # Fallback: planare Projektion entlang Normalen
            n=sum((f.normal for f in fs),Vector()).normalized(); t=n.orthogonal().normalized(); bt=n.cross(t)
            P=np.array([[l.vert.co.dot(t),l.vert.co.dot(bt)] for l in loops]); sc_=1.0
        else:
            sc_=math.sqrt(a3/ua); P=P*sc_
        c=P.mean(0); Q=P-c
        if len(Q)>2:
            w,v=np.linalg.eigh(np.cov(Q.T)); Q=Q@v
        Q=(Q-Q.min(0))*boost; wh=Q.max(0)
        if wh[1]>wh[0]: Q=Q[:,::-1]; wh=wh[::-1]
        rects.append([loops,Q,wh,uvl])
    def place(k):
        x=y=sh=0.0; pos=[]
        for loops,Q,wh,uvl in sorted(rects,key=lambda r:-r[2][1]):
            w=wh[0]*k+pad_uv; h=wh[1]*k+pad_uv
            if x+w>1.0: x=0.0; y+=sh; sh=0.0
            if w>1.0 or y+h>1.0: return None
            pos.append((loops,Q,uvl,(x+pad_uv/2,y+pad_uv/2))); x+=w; sh=max(sh,h)
        return pos
    lo,hi=0.0,1e4; best=None
    for _ in range(40):
        m=(lo+hi)/2; p=place(m)
        if p: lo=m; best=p
        else: hi=m
    for loops,Q,uvl,(ox,oy) in best:
        for l,q in zip(loops,Q): l[uvl].uv=(ox+q[0]*lo,oy+q[1]*lo)
    for o,bm in bms: bm.to_mesh(o.data); bm.free()
    return lo,len(rects)
k,ni=pack_uniform(lows,PAD/TEX); log("UV gepackt: Inseln",ni,"Texeldichte px/m",round(k*TEX),"Padding px",PAD)
# ---- Bake-Setup
sc.render.engine='CYCLES'; sc.cycles.device='CPU'; sc.cycles.samples=1
bk=sc.render.bake; bk.margin=PAD//2; bk.margin_type='EXTEND'
def newimg(n,cs='Non-Color'):
    im=bpy.data.images.new(f"T_{NM}_LOD{LI}_{n}",TEX,TEX); im.colorspace_settings.name=cs; return im
BM=bpy.data.materials.new("BAKE"); BM.use_nodes=True; tn=BM.node_tree.nodes.new("ShaderNodeTexImage")
def dupjoin(objs,name,dx=0.0):
    cs=[]
    for i,o in enumerate(objs):
        c=o.copy(); c.data=o.data.copy(); sc.collection.objects.link(c); c.location.x+=i*dx; cs.append(c)
    for o in sc.objects: o.select_set(False)
    for c in cs: c.select_set(True)
    bpy.context.view_layer.objects.active=cs[0]; bpy.ops.object.join(); j=bpy.context.active_object; j.name=name; return j
EX=0.4
BL=dupjoin(lows,"BAKE_LOW",EX)
for i,k in enumerate(keys): H[k].location.x+=i*EX
for o in sc.objects: o.select_set(False)
for k in keys: H[k].select_set(True)
bpy.context.view_layer.objects.active=H[keys[0]]; bpy.ops.object.join(); BH=bpy.context.active_object; BH.name="BAKE_HIGH"
for o in [o for o in bpy.data.objects if o.name.startswith("H_") and o!=BH]: bpy.data.objects.remove(o)
# Low-Materialslots: Bake-Bild in jedem Slot aktiv
def set_target(obj,img):
    tn.image=img
    for s in obj.material_slots:
        M=s.material; nt=M.node_tree
        t=nt.nodes.get("BAKETEX") or nt.nodes.new("ShaderNodeTexImage"); t.name="BAKETEX"; t.image=img; nt.nodes.active=t
def bake(kind,img,obj,s2a,**kw):
    set_target(obj,img)
    for o in sc.objects: o.select_set(False)
    if s2a: BH.select_set(True)
    obj.select_set(True); bpy.context.view_layer.objects.active=obj
    bk.use_selected_to_active=s2a; ext=2*L["lin"]/1000+0.0005; bk.cage_extrusion=ext; bk.max_ray_distance=3*ext
    bpy.ops.object.bake(type=kind,**kw); pxv=np.array(img.pixels[:]).reshape(-1,4); log("bake",kind,img.name,pxv.mean(0).round(3),"uvs",[u.name for u in obj.data.uv_layers])
def save(img):
    img.filepath_raw=f"{OUT}/textures/{img.name}.png"; img.file_format='PNG'; img.save()
def decal_nodes(M,dc,k):
    """Aufdruck per Projektion (Weltkoordinaten): 'cyl' = Abwicklung um Rohrachse, 'planar_x' = Seitenansicht ±X."""
    nt=M.node_tree; N=nt.nodes; Lk=nt.links
    if "DMIX" in N: return N["DMIX"]
    geo=N.new("ShaderNodeNewGeometry"); sp=N.new("ShaderNodeSeparateXYZ"); Lk.new(geo.outputs["Position"],sp.inputs[0])
    def m(op,a,b=None,val=None):
        n=N.new("ShaderNodeMath"); n.operation=op
        for i,x in enumerate((a,b)):
            if x is None: continue
            if isinstance(x,(int,float)): n.inputs[i].default_value=x
            else: Lk.new(x,n.inputs[i])
        return n.outputs[0]
    me=Lo[k].data; ys=[v.co.y for v in me.vertices]
    y0=dc.get("y0",min(ys)); y1=dc.get("y1",max(ys))
    if dc["type"]=="cyl":
        dx=m('SUBTRACT',sp.outputs[0],axis0.x); dz=m('SUBTRACT',sp.outputs[2],axis0.z)
        ang=m('ARCTAN2',dx,dz); u=m('MULTIPLY',ang,dc.get("u_sign",1)/(2*math.pi)); u=m('ADD',u,dc.get("u_offset",0.0))
        v=m('DIVIDE',m('SUBTRACT',sp.outputs[1],y0),y1-y0)
        if dc.get("v_flip"): v=m('SUBTRACT',1.0,v)
        mask=None
    else:
        sd=dc.get("side",0); z0,z1=dc["z0"],dc["z1"]   # side: +1/-1 = nur diese Seite, 0 = beide (lesbar gespiegelt)
        sn=N.new("ShaderNodeSeparateXYZ"); Lk.new(geo.outputs["Normal"],sn.inputs[0])
        u=m('DIVIDE',m('SUBTRACT',sp.outputs[1],y0),y1-y0)
        sg=m('SIGN',sn.outputs[0]) if sd==0 else sd
        u=m('ADD',m('MULTIPLY',m('SUBTRACT',u,0.5),sg),0.5)
        v=m('DIVIDE',m('SUBTRACT',sp.outputs[2],z0),z1-z0)
        mask=m('GREATER_THAN',m('ABSOLUTE',sn.outputs[0]),0.6) if sd==0 else m('GREATER_THAN',m('MULTIPLY',sn.outputs[0],sd),0.6)
    cb=N.new("ShaderNodeCombineXYZ"); Lk.new(u,cb.inputs[0]); Lk.new(v,cb.inputs[1])
    tx=N.new("ShaderNodeTexImage"); tx.name="DTEX"; tx.image=bpy.data.images.load(dc["image"]); tx.extension='REPEAT' if dc["type"]=="cyl" else 'CLIP'
    tx.interpolation='Cubic'; Lk.new(cb.outputs[0],tx.inputs[0])
    fac=tx.outputs["Alpha"]
    if mask is not None: fac=m('MULTIPLY',fac,mask)
    mix=N.new("ShaderNodeMix"); mix.data_type='RGBA'; mix.name="DMIX"; Lk.new(fac,mix.inputs["Factor"])
    return mix
def emit_mode(fn,kind="color"):
    mats=[(k,M) for k,M in SRC.items()]+[(c,bpy.data.materials[n]) for n,(c,dc,k) in DEC.items()]
    for k,M in mats:
        nt=M.node_tree; e=nt.nodes.get("EM") or nt.nodes.new("ShaderNodeEmission"); e.name="EM"
        val=fn(cfg["materials"][k])
        if M.name in DEC:
            c_,dc,pk=DEC[M.name]; mix=decal_nodes(M,dc,pk)
            mix.inputs[6].default_value=val
            for l in list(mix.inputs[7].links): nt.links.remove(l)
            if kind=="color": nt.links.new(nt.nodes["DTEX"].outputs["Color"],mix.inputs[7])
            elif kind=="rough": mix.inputs[7].default_value=(dc.get("rough",0.5),)*3+(1,)
            else: mix.inputs[7].default_value=(0,0,0,1)
            nt.links.new(mix.outputs[2],e.inputs[0])
        else:
            for l in list(e.inputs[0].links): nt.links.remove(l)
            e.inputs[0].default_value=val
        nt.links.new(e.outputs[0],nt.nodes["Material Output"].inputs[0])
def bsdf_mode():
    for k,M in list(SRC.items())+[(c,bpy.data.materials[n]) for n,(c,dc,_k) in DEC.items()]:
        v=cfg["materials"][k]; nt=M.node_tree; b=nt.nodes["Principled BSDF"]
        b.inputs["Base Color"].default_value=(*v["color"],1); b.inputs["Metallic"].default_value=v["metal"]; b.inputs["Roughness"].default_value=v["rough"]
        nt.links.new(b.outputs[0],nt.nodes["Material Output"].inputs[0])
bsdf_mode()
sc.cycles.samples=cfg.get("bake_samples",16)
IM={}
IM["Normal"]=newimg("Normal"); bake('NORMAL',IM["Normal"],BL,True); save(IM["Normal"])
BL2=dupjoin(lows,"BAKE_LOW_INPLACE",0.0)  # Weltlage nötig für Aufdruck-Projektion
emit_mode(lambda v:(*v["color"],1),"color"); IM["BaseColor"]=newimg("BaseColor",'sRGB'); bake('EMIT',IM["BaseColor"],BL2,False); save(IM["BaseColor"])
emit_mode(lambda v:(v["rough"],)*3+(1,),"rough"); IR=newimg("R"); bake('EMIT',IR,BL2,False)
emit_mode(lambda v:(v["metal"],)*3+(1,),"metal"); IMt=newimg("M"); bake('EMIT',IMt,BL2,False)
bsdf_mode()
sc.cycles.samples=48
sc.world=bpy.data.worlds.new("w"); sc.world.light_settings.distance=0.02
IA1=newimg("AO_detail"); bake('AO',IA1,BL,True)
# AO zwischen Teilen: Lows an Originalposition
IA2=newimg("AO_contact"); bake('AO',IA2,BL2,False)
px=lambda im: np.array(im.pixels[:],dtype=np.float32).reshape(TEX,TEX,4)
ao=px(IA1)[...,0]*(0.35+0.65*px(IA2)[...,0])
IAO=newimg("AO"); a=np.ones((TEX,TEX,4),np.float32); a[...,:3]=ao[...,None]; IAO.pixels[:]=a.ravel(); save(IAO)
orm=np.ones((TEX,TEX,4),np.float32); orm[...,0]=ao; orm[...,1]=px(IR)[...,0]; orm[...,2]=px(IMt)[...,0]
IO=newimg("ORM"); IO.pixels[:]=orm.ravel(); save(IO)
n=px(IM["Normal"]).copy(); n[...,1]=1-n[...,1]; ID=newimg("Normal_DirectX"); ID.pixels[:]=n.ravel(); save(ID)
for o in (BL,BL2,BH): bpy.data.objects.remove(o)
for im in (IR,IMt,IA1,IA2): bpy.data.images.remove(im)
# ---- Finales Material
FM=bpy.data.materials.new(f"M_{NM}_LOD{LI}"); FM.use_nodes=True; nd=FM.node_tree.nodes; lk=FM.node_tree.links; P=nd["Principled BSDF"]
def tx(img,y):
    t=nd.new("ShaderNodeTexImage"); t.image=img; t.location=(-700,y); return t
lk.new(tx(IM["BaseColor"],300).outputs[0],P.inputs["Base Color"])
sp=nd.new("ShaderNodeSeparateColor"); sp.location=(-350,0); lk.new(tx(IO,0).outputs[0],sp.inputs[0])
lk.new(sp.outputs[1],P.inputs["Roughness"]); lk.new(sp.outputs[2],P.inputs["Metallic"])
nm=nd.new("ShaderNodeNormalMap"); nm.location=(-350,-300); lk.new(tx(IM["Normal"],-300).outputs[0],nm.inputs[1]); lk.new(nm.outputs[0],P.inputs["Normal"])
# ---- Gruppen, Pivots, Collections
col=bpy.data.collections.new(f"LOD{LI}"); sc.collection.children.link(col)
assign={}
for k in keys: assign.setdefault(grp(k)["name"],[]).append(k)
def bbc(objs):
    vs=[o.matrix_world@v.co for o in objs for v in o.data.vertices]
    return Vector([(min(v[i] for v in vs)+max(v[i] for v in vs))/2 for i in range(3)])
info=[]
for g in cfg["groups"]:
    ks=assign.get(g["name"],[]);
    if not ks: continue
    objs=[Lo[k] for k in ks]; c=bbc(objs); pv=g["pivot"]
    if pv=="origin": p=Vector((0,0,0)); ax="—"
    elif pv=="barrel_axis": p=Vector((axis0.x,c.y,axis0.z)); ax="Y (Rohrachse)"
    elif pv.startswith("axis_between:"):
        s=pv.split(":")[1]; pts=[bbc([Lo[k]]) for k in ks if s in k]; p=sum(pts,Vector())/len(pts); ax="X (Hebelachse)"
    for o in sc.objects: o.select_set(False)
    for o in objs: o.select_set(True)
    bpy.context.view_layer.objects.active=objs[0]; bpy.ops.object.join(); o=bpy.context.active_object
    o.name=o.data.name=f"SM_{NM}_{g['name']}_LOD{LI}"
    o.vertex_groups.clear(); o.data.materials.clear(); o.data.materials.append(FM)
    o.data.transform(Matrix.Translation(-p)); o.location=p
    sc.collection.objects.unlink(o); col.objects.link(o)
    info.append({"name":o.name,"tris":tris(o),"pivot_m":[round(x,4) for x in p],"achse":ax,"teile":[re.sub(r"^NAUO\d+\|","",k) for k in ks]})
for o in list(sc.objects):
    if o.name.startswith("L_"): bpy.data.objects.remove(o)
for M in list(SRC.values())+[bpy.data.materials[n] for n in DEC]: bpy.data.materials.remove(M)
bpy.data.materials.remove(BM)
json.dump({"lod":LI,"tex":TEX,"tris":sum(i["tris"] for i in info),"objekte":info},open(f"{W}/LOD{LI}_info.json","w"),indent=1,ensure_ascii=False)
log("LOD",LI,"tris",sum(i["tris"] for i in info))
bpy.ops.file.pack_all()
bpy.ops.wm.save_as_mainfile(filepath=f"{W}/LOD{LI}.blend",compress=True)
# Export
os.makedirs(OUT+"/export",exist_ok=True)
for o in sc.objects: o.select_set(o.name.startswith("SM_"))
bpy.ops.export_scene.fbx(filepath=f"{OUT}/export/SM_{NM}_LOD{LI}.fbx",use_selection=True,apply_unit_scale=True,apply_scale_options='FBX_SCALE_UNITS',axis_forward='-Z',axis_up='Y',mesh_smooth_type='OFF',use_tspace=True,path_mode='COPY',embed_textures=True)
bpy.ops.export_scene.gltf(filepath=f"{OUT}/export/SM_{NM}_LOD{LI}.glb",use_selection=True,export_format='GLB')
log("DONE")
