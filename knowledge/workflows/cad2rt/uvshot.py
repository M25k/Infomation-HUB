"""cad2rt/uvshot.py – UV-Layout über BaseColor zeichnen (ohne GPU). Aufruf: blender -b X.blend --python uvshot.py -- OUTDIR PREFIX"""
import bpy,sys,json,os,subprocess
a=sys.argv[sys.argv.index("--")+1:]
for c in [c for c in bpy.data.collections if c.name.startswith("LOD")]:
    objs=[o for o in c.objects if o.type=='MESH']; polys=[]
    for o in objs:
        uv=o.data.uv_layers.active.data; polys+=[[tuple(uv[i].uv) for i in p.loop_indices] for p in o.data.polygons]
    im=objs[0].data.materials[0].node_tree.nodes["Principled BSDF"].inputs["Base Color"].links[0].from_node.image
    p=bpy.path.abspath(f"/tmp/{c.name}_bc.png"); im.save(filepath=p)
    json.dump(polys,open(f"/tmp/{c.name}_uv.json","w"))
    subprocess.run([os.environ.get("CAD2RT_PY","python3"),"-c",f"""
import json;from PIL import Image,ImageDraw
im=Image.open('/tmp/{c.name}_bc.png').convert('RGB');S=im.size[0];im=im.resize((2048,2048));im=im.point(lambda v:int(v*0.6+60));d=ImageDraw.Draw(im)
for f in json.load(open('/tmp/{c.name}_uv.json')): d.polygon([(u*2048,(1-v)*2048) for u,v in f],outline=(0,255,255))
im.save('{a[0]}/{a[1]}UV_{c.name}_'+str(S)+'px.png')"""])
