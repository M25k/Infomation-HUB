"""cad2rt/assemble.py – fasst LOD-Blends zu einer gepackten Master-.blend zusammen.
Aufruf: blender -b --python assemble.py -- CONFIG.json"""
import bpy,sys,json
cfg=json.load(open(sys.argv[sys.argv.index("--")+1])); W=cfg["work"]; OUT=cfg["out"]
bpy.ops.wm.read_factory_settings(use_empty=True); sc=bpy.context.scene
for i in range(len(cfg["lods"])):
    with bpy.data.libraries.load(f"{W}/LOD{i}.blend",link=False) as (src,dst): dst.collections=[f"LOD{i}"]
    for c in dst.collections:
        sc.collection.children.link(c)
        if i>0: bpy.context.view_layer.layer_collection.children[c.name].hide_viewport=True
bpy.ops.file.pack_all()
bpy.ops.wm.save_as_mainfile(filepath=f"{OUT}/{cfg['name']}_v2.blend",compress=True)
