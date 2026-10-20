"""cad2rt/make_decals.py – erzeugt Aufdruck-Texturen (RGBA, transparent) (Beispiel: Strahlrohr mit Skalenring und Gehäuse-Beschriftung).
Generisch nutzbar als Vorlage: Texte/Positionen anpassen. Aufruf: python make_decals.py OUTDIR"""
import sys, os, math
from PIL import Image, ImageDraw, ImageFont
OUT=sys.argv[1]; os.makedirs(OUT,exist_ok=True)
FB="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"; FR="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
LOGO_TEXT=os.environ.get("CAD2RT_LOGO_TEXT","LOGO")
WHITE=(245,245,245,255); BLACK=(15,15,15,255)
# 1) Skalenring: Abwicklung 360° (u=Winkel ab Oberseite, v=axial). Ring ~Ø62 x 16 mm -> 4096 x 336 px (~21 px/mm)
W,H=4096,336; im=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
f=ImageFont.truetype(FB,190); fs=ImageFont.truetype(FB,90)
def at(deg): return int((deg%360)/360*W)
for txt,deg in [("300",0),("200",-55),("100",-110)]:
    x=at(deg); bb=d.textbbox((0,0),txt,font=f); w=bb[2]-bb[0]
    for xx in (x,x+W,x-W): d.text((xx-w//2,H//2-120),txt,font=f,fill=WHITE)
    # Markierungsdreieck neben der Zahl
    tx=(x+w//2+60)%W; d.polygon([(tx,H//2+40),(tx+50,H//2+40),(tx+25,H//2-10)],fill=WHITE)
x=at(70); d.text((x-180,H//2-55),"FLUSH",font=fs,fill=WHITE)
for k in range(3): d.polygon([(x+150+k*45,H//2-40),(x+150+k*45,H//2+40),(x+185+k*45,H//2)],fill=WHITE)
im.save(f"{OUT}/D_Skalenring.png")
# 2) Gehäuse-Seite: CLOSE | Herstellerlogo (Platzhalter) | OPEN  (Fläche 50 x 18 mm -> 2000 x 720 px, 40 px/mm)
W,H=2000,720; im=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
fl=ImageFont.truetype(FB,92)
def label(cx,txt):
    bb=d.textbbox((0,0),txt,font=fl); w=bb[2]-bb[0]; h=bb[3]-bb[1]
    d.rectangle((cx-w//2-30,H//2-h//2-40,cx+w//2+30,H//2+h//2+40),fill=WHITE)
    d.text((cx-w//2,H//2-h//2-bb[1]),txt,font=fl,fill=BLACK)
label(330,"CLOSE"); label(1670,"OPEN")
# Logo-Platzhalter: weißer Rahmen, kursiver Text LOGO_TEXT (Scherung); echtes Herstellerlogo nur intern einsetzen
lg=Image.new("RGBA",(560,560),(0,0,0,0)); g=ImageDraw.Draw(lg)
g.rectangle((10,10,550,550),outline=WHITE,width=22)
fa=ImageFont.truetype(FB,230); bb=g.textbbox((0,0),LOGO_TEXT,font=fa)
t=Image.new("RGBA",(bb[2]+80,bb[3]+40),(0,0,0,0)); ImageDraw.Draw(t).text((40,0),LOGO_TEXT,font=fa,fill=WHITE)
t=t.transform(t.size,Image.AFFINE,(1,0.25,-40,0,1,0),Image.BICUBIC)
t.thumbnail((470,470)); lg.alpha_composite(t,((560-t.width)//2,(560-t.height)//2+20))
lg=lg.resize((420,420),Image.LANCZOS); im.alpha_composite(lg,(W//2-210,H//2-210))
im.save(f"{OUT}/D_Gehaeuse_Seite.png")
print("ok")
