#!/usr/bin/env bash
# cad2rt – komplette Pipeline STEP -> Echtzeit-Asset. Aufruf: ./run_all.sh CONFIG.json
set -euo pipefail
C=$(cd "$(dirname "$0")" && pwd); CFG=$(realpath "$1")
PY=${CAD2RT_PY:-python3}   # venv mit cadquery-ocp, numpy, pillow
j(){ $PY -c "import json,sys;c=json.load(open('$CFG'));print(eval(sys.argv[1]))" "$1"; }
W=$(j 'c["work"]'); OUT=$(j 'c["out"]'); STEP=$(j 'c["step"]'); SK=$(j 'c["skip_regex"]'); N=$(j 'len(c["lods"])')
mkdir -p "$W" "$OUT/screenshots"
DS=$(j 'c.get("decals_script","")'); DD=$(j 'c.get("decals_dir","")')
[ -n "$DS" ] && $PY "$DS" "$DD"      # Aufdruck-Texturen erzeugen (optional)
$PY $C/tess.py "$STEP" "$W/HIGH" --lin $(j 'c["high"]["lin"]') --ang $(j 'c["high"]["ang"]') --normals --skip "$SK" > "$W/HIGH.log"
for i in $(seq 0 $((N-1))); do
  $PY $C/tess.py "$STEP" "$W/L$i" --lin $(j "c['lods'][$i]['lin']") --ang $(j "c['lods'][$i]['ang']") --skip "$SK" > "$W/L$i.log" &
done; wait
for i in $(seq 0 $((N-1))); do blender -b --python $C/build_lod.py -- "$CFG" $i > "$W/build$i.log" 2>&1; done
blender -b --python $C/assemble.py -- "$CFG" > "$W/assemble.log" 2>&1
B="$OUT/$(j 'c["name"]')_$(j 'c.get("version","v2")').blend"
SHOTS=gesamt,detail,wire blender -b "$B" --python $C/shots.py -- "$OUT/screenshots" "" "$W/cams.json" > "$W/shots.log" 2>&1
blender -b "$B" --python $C/uvshot.py -- "$OUT/screenshots" "" > "$W/uv.log" 2>&1
grep -h "LOD .* tris\|UV gepackt\|VOXEL\|WARNUNG" "$W"/build*.log
