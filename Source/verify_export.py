from pathlib import Path
import json,time
import cadquery as cq
import trimesh
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
info=json.loads((ROOT/'Checks/Components.json').read_text())
p=ROOT/'CAD/Marble_Mayhem_V2_assembled.step'
s=cq.importers.importStep(str(p)).val();b=s.BoundingBox()
rep={'step_file':p.name,'read_back_success':True,'shape_valid':s.isValid(),'solid_count':len(s.Solids()),'named_component_count':len(info),'source_valid_components':sum(a['valid'] for a in info),'total_dimensions_mm':[b.xlen,b.ylen,b.zlen],'nominal_marble_diameter_mm':10,'printable_component_volume_cm3':sum(a['volume_mm3'] for a in info if a['printable'])/1000,'new_or_modified_component_count':sum(a['changed'] for a in info),'caveat':'File and geometric checks only. Not roll-tested or print-tested; no budget quote.'}
rep['solid_PLA_equivalent_g_at_assumed_density_1_24']=rep['printable_component_volume_cm3']*1.24
(ROOT/'Checks/STEP_import_validation.json').write_text(json.dumps(rep,indent=2));print(json.dumps(rep,indent=2),flush=True)
meshes=[]
for it in info:
 if not it['printable']:continue
 path=ROOT/'STL_Prototype'/(it['name']+'.stl')
 m=trimesh.load_mesh(str(path),process=True)
 meshes.append({'part':it['name'],'changed':it['changed'],'triangle_count':len(m.faces),'watertight_mesh':bool(m.is_watertight),'winding_consistent':bool(m.is_winding_consistent)})
(ROOT/'Checks/STL_mesh_validation.json').write_text(json.dumps({'note':'Closed-shell checks do not establish continuous assembled rail unions or FDM suitability. Intersecting subsolids need slicer review/union.','meshes':meshes},indent=2))
print('MESH_CHECKS',sum(a['watertight_mesh'] for a in meshes),'of',len(meshes),flush=True)
