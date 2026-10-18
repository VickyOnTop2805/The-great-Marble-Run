from pathlib import Path
import json,numpy as np,cadquery as cq
ROOT=Path(__file__).resolve().parents[1]
info=json.loads((ROOT/'Checks/Components.json').read_text())
paths=json.loads((ROOT/'Checks/Nominal_marble_paths.json').read_text())
C={'black':(.075,.080,.085),'blue':(.025,.13,.69),'orange':(1.,.30,.018),'green':(.24,.82,.035),'silver':(.68,.72,.77),'clear':(.66,.80,.88)}
shapes={}
for it in info:
 name=it['name'];s=cq.importers.importStep(str(ROOT/'CAD/Components'/(name+'.step'))).val()
 if name=='DISPLAY_Plinko_ball':
  p=paths['35_Example_Plinko_clear_corridor_NOT_dynamics'][76]
  s=cq.Solid.makeSphere(5,cq.Vector(*p),angleDegrees1=-90,angleDegrees2=90)
  cq.exporters.export(s,str(ROOT/'CAD/Components'/(name+'.step')))
  v,f=s.tessellate(.12,.22);np.savez_compressed(ROOT/'Checks/mesh_cache'/(name+'.npz'),vertices=np.array([[a.x,a.y,a.z] for a in v]),faces=np.array(f))
  b=s.BoundingBox();it['bounds_mm']=[b.xmin,b.xmax,b.ymin,b.ymax,b.zmin,b.zmax]
 shapes[name]=s
assembly=cq.Assembly(name='Marble_Mayhem_V2_Funnel_Link_Plinko_Column')
for it in info:assembly.add(shapes[it['name']],name=it['name'],color=cq.Color(*C[it['col']],.45 if it['col']=='clear' else 1.))
assembly.export(str(ROOT/'CAD/Marble_Mayhem_V2_assembled.step'))
(ROOT/'Checks/Components.json').write_text(json.dumps(info,indent=2))
pairs=[('30_Green_ladder_to_funnel_bridge','07_Green_upper_snaking_rails'),('30_Green_ladder_to_funnel_bridge','31_Green_funnel_entry_chute'),('31_Green_funnel_entry_chute','02_Orange_funnel'),('34a_Green_two_way_route_selector','08_Orange_transfer_scoop'),('34a_Green_two_way_route_selector','09_Green_return_to_steps'),('34a_Green_two_way_route_selector','34b_Green_selector_to_Plinko_chute'),('34b_Green_selector_to_Plinko_chute','35_Orange_Plinko_board_with_pegs'),('35_Orange_Plinko_board_with_pegs','37_Green_Plinko_return_to_catcher'),('40_Orange_central_spiral_column_and_arms','05_Green_front_vortex'),('40_Orange_central_spiral_column_and_arms','01_Base_right')]
rep=[]
for a,b in pairs:
 dist=shapes[a].distance(shapes[b]);rep.append({'part_1':a,'part_2':b,'minimum_surface_separation_mm':dist});print('CONTACT',a,b,dist,flush=True)
(ROOT/'Checks/New_part_contact_distances.json').write_text(json.dumps({'description':'Minimum native CAD surface distances at intended non-drop joins. Does not prove mechanical fit/adhesion/strength.','pairs':rep},indent=2))
print('FINAL_ASSEMBLY_EXPORTED',flush=True)
