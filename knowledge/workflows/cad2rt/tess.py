"""cad2rt/tess.py – STEP -> OBJ (ein Objekt pro Bauteil-Instanz) + Kanten-JSON (CAD-Flächengrenzen, periodische Nähte).
Aufruf: python tess.py IN.step OUT_PREFIX --lin 0.05 --ang 0.3 [--scale 0.001] [--normals]
Lizenz: OCCT (LGPL-2.1+Ausnahme) via cadquery-ocp (Apache-2.0)."""
import sys, json, argparse, re
from OCP.STEPCAFControl import STEPCAFControl_Reader
from OCP.TDocStd import TDocStd_Document
from OCP.TCollection import TCollection_ExtendedString
from OCP.XCAFDoc import XCAFDoc_DocumentTool
from OCP.collections import Sequence_TDF_Label as Seq
from OCP.TDF import TDF_Label
from OCP.TDataStd import TDataStd_Name
from OCP.BRepMesh import BRepMesh_IncrementalMesh
from OCP.TopExp import TopExp_Explorer
from OCP.TopAbs import TopAbs_FACE, TopAbs_EDGE, TopAbs_REVERSED
from OCP.BRep import BRep_Tool
from OCP.TopLoc import TopLoc_Location
from OCP.TopoDS import TopoDS
from OCP.BRepLib import BRepLib_ToolTriangulatedShape
ap=argparse.ArgumentParser(); ap.add_argument("step"); ap.add_argument("out")
ap.add_argument("--lin",type=float,default=0.05); ap.add_argument("--ang",type=float,default=0.3)
ap.add_argument("--scale",type=float,default=0.001); ap.add_argument("--normals",action="store_true")
ap.add_argument("--skip",default="",help="Regex: Bauteile nicht tesselieren")
a=ap.parse_args(); S=a.scale
doc=TDocStd_Document(TCollection_ExtendedString("doc"))
r=STEPCAFControl_Reader(); r.SetNameMode(True); assert r.ReadFile(a.step)==1; r.Transfer(doc)
st=XCAFDoc_DocumentTool.ShapeTool_s(doc.Main())
def name(l):
    n=TDataStd_Name(); return n.Get().ToExtString() if l.FindAttribute(TDataStd_Name.GetID_s(),n) else "x"
parts=[]
def walk(lab,loc,pn):
    if st.IsReference_s(lab):
        rl=TDF_Label(); st.GetReferredShape_s(lab,rl); walk(rl,loc.Multiplied(st.GetLocation_s(lab)),name(lab)); return
    if st.IsAssembly_s(lab):
        s=Seq(); st.GetComponents_s(lab,s)
        for i in range(1,s.Length()+1): walk(s.Value(i),loc,pn)
        return
    parts.append((pn+"|"+name(lab),st.GetShape_s(lab).Moved(loc)))
roots=Seq(); st.GetFreeShapes(roots)
for i in range(1,roots.Length()+1): walk(roots.Value(i),TopLoc_Location(),"root")
skip=re.compile(a.skip) if a.skip else None
out=open(a.out+".obj","w"); edges={}; vo=1; no=1; stats=[]
R=lambda p:(round(p.X()*S,6),round(p.Y()*S,6),round(p.Z()*S,6))
for n,s in parts:
    safe=re.sub(r"[^A-Za-z0-9_|.~-]","_",n)
    if skip and skip.search(n): continue
    BRepMesh_IncrementalMesh(s,a.lin,False,a.ang,True)
    out.write(f"o {safe}\n"); ed=[]; nt=0
    e=TopExp_Explorer(s,TopAbs_FACE)
    while e.More():
        f=TopoDS.Face(e.Current()); L=TopLoc_Location(); tri=BRep_Tool.Triangulation_s(f,L)
        if tri:
            tr=L.Transformation(); rev=f.Orientation()==TopAbs_REVERSED
            if a.normals: BRepLib_ToolTriangulatedShape.ComputeNormals_s(f,tri)
            P=[tri.Node(i).Transformed(tr) for i in range(1,tri.NbNodes()+1)]
            for p in P: out.write("v %.7f %.7f %.7f\n"%(p.X()*S,p.Y()*S,p.Z()*S))
            if a.normals:
                for i in range(1,tri.NbNodes()+1):
                    d=tri.Normal(i).Transformed(tr)
                    if rev: d.Reverse()
                    out.write("vn %.5f %.5f %.5f\n"%(d.X(),d.Y(),d.Z()))
            for i in range(1,tri.NbTriangles()+1):
                x,y,z=tri.Triangle(i).Get()
                if rev: y,z=z,y
                if a.normals: out.write(f"f {x+vo-1}//{x+no-1} {y+vo-1}//{y+no-1} {z+vo-1}//{z+no-1}\n")
                else: out.write(f"f {x+vo-1} {y+vo-1} {z+vo-1}\n")
                nt+=1
            ee=TopExp_Explorer(f,TopAbs_EDGE)
            while ee.More():
                E=TopoDS.Edge(ee.Current()); per=BRep_Tool.IsClosed_s(E,f)
                pol=BRep_Tool.PolygonOnTriangulation_s(E,tri,L)
                if pol:
                    idx=[pol.Node(k) for k in range(1,pol.NbNodes()+1)]
                    for k in range(len(idx)-1): ed.append([R(P[idx[k]-1]),R(P[idx[k+1]-1]),1 if per else 0])
                ee.Next()
            vo+=len(P); no+=len(P)
        e.Next()
    edges[safe]=ed; stats.append((safe,nt)); print(f"{safe}\t{nt}")
json.dump(edges,open(a.out+"_edges.json","w"))
print("TOTAL",sum(t for _,t in stats))
