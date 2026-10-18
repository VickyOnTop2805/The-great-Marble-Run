from pathlib import Path
import os,json,math,time
import numpy as np
import vtk
from vtk.util.numpy_support import numpy_to_vtk,numpy_to_vtkIdTypeArray
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parents[1]
C={'black':(.075,.080,.085),'blue':(.025,.13,.69),'orange':(1.,.30,.018),'green':(.24,.82,.035),'silver':(.68,.72,.77),'clear':(.66,.80,.88)}
info=json.loads((ROOT/'Checks/Components.json').read_text());paths=json.loads((ROOT/'Checks/Nominal_marble_paths.json').read_text())
def poly(v,f):
 pts=vtk.vtkPoints();pts.SetData(numpy_to_vtk(v,deep=True))
 cells=vtk.vtkCellArray();arr=np.c_[np.full(len(f),3),f].astype(np.int64)
 cells.SetCells(len(f),numpy_to_vtkIdTypeArray(arr.ravel(),deep=True))
 pd=vtk.vtkPolyData();pd.SetPoints(pts);pd.SetPolys(cells);return pd
meshes={};fields={};bounds={}
for it in info:
 data=np.load(ROOT/'Checks/mesh_cache'/(it['name']+'.npz'));pd=poly(data['vertices'],data['faces']);meshes[it['name']]=pd
 if it['group']!='Display_balls':
  field=vtk.vtkImplicitPolyDataDistance();field.SetInput(pd);fields[it['name']]=field
  b=np.array(pd.GetBounds());bounds[it['name']]=(b[[0,2,4]],b[[1,3,5]])
# Render actual CAD geometry, not a made-up Onshape screenshot.
rend=vtk.vtkRenderer();rend.SetBackground(1,1,1)
actors={}
for it in info:
 pd=meshes[it['name']]
 norm=vtk.vtkPolyDataNormals();norm.SetInputData(pd);norm.SetFeatureAngle(45);norm.SplittingOn();norm.ConsistencyOn();norm.Update()
 mp=vtk.vtkPolyDataMapper();mp.SetInputConnection(norm.GetOutputPort());mp.ScalarVisibilityOff()
 ac=vtk.vtkActor();ac.SetMapper(mp);pr=ac.GetProperty();pr.SetColor(*C[it['col']]);pr.SetAmbient(.29);pr.SetDiffuse(.64);pr.SetSpecular(.22 if it['col']=='silver' else .13);pr.SetSpecularPower(35);pr.SetInterpolationToPhong()
 if it['col']=='clear':pr.SetOpacity(.4)
 rend.AddActor(ac);actors[it['name']]=ac
 if it['group']!='Display_balls':
  ed=vtk.vtkFeatureEdges();ed.SetInputData(pd);ed.BoundaryEdgesOn();ed.FeatureEdgesOn();ed.SetFeatureAngle(45);ed.ManifoldEdgesOff();ed.NonManifoldEdgesOff();em=vtk.vtkPolyDataMapper();em.SetInputConnection(ed.GetOutputPort());em.ScalarVisibilityOff();ea=vtk.vtkActor();ea.SetMapper(em);ea.GetProperty().SetColor(.09,.13,.10);ea.GetProperty().SetLineWidth(.65);rend.AddActor(ea)
win=vtk.vtkRenderWindow();win.SetOffScreenRendering(1);win.SetSize(1500,1500);win.SetMultiSamples(4);win.AddRenderer(rend)
cam=rend.GetActiveCamera();cam.SetParallelProjection(True);cam.SetViewUp(0,0,1)
fontfile='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
font=ImageFont.truetype(fontfile,20)
def render(name,pos,focus,scale,label):
 cam.SetViewUp(*((0,1,0) if pos[0]==0 and pos[1]==0 else (0,0,1)));cam.SetPosition(*pos);cam.SetFocalPoint(*focus);cam.SetParallelScale(scale);rend.ResetCameraClippingRange();win.Render()
 img=vtk.vtkWindowToImageFilter();img.SetInput(win);img.ReadFrontBufferOff();img.Update();wr=vtk.vtkPNGWriter();wr.SetFileName(str(ROOT/name));wr.SetInputConnection(img.GetOutputPort());wr.Write()
 im=Image.open(ROOT/name).convert('RGB');dr=ImageDraw.Draw(im);dr.rectangle((0,1437,1500,1500),fill='white');dr.text((28,1456),label,font=font,fill='#25302d');im.save(ROOT/name)
render('Preview_Updated_Assembly.png',(-340,-530,440),(0,2,101),190,'ACTUAL CAD | New funnel bridge + Plinko route + central spiral support | Prototype')
render('Preview_Rear_Bridge.png',(-280,530,425),(0,12,101),180,'ACTUAL CAD | Rear bridge: ladder loading point to funnel | Prototype')
render('Preview_Plinko_Column.png',(-310,-500,400),(-16,-15,77),117,'ACTUAL CAD | Plinko branch, shared catcher and spiral support column | Prototype')
render('Preview_Top.png',(0,0,650),(0,0,0),155,'ACTUAL CAD | Top view | Geometric prototype; not physically tested')
print('RENDERS_DONE',flush=True)
# Clearance is a geometric surface test for nominal 10mm spheres, NOT a dynamic test.
reports=[];hits=[]
for name,data in paths.items():
 p=np.array(data,float);s=np.r_[0,np.cumsum(np.linalg.norm(np.diff(p,axis=0),axis=1))];u=np.linspace(0,s[-1],max(30,math.ceil(s[-1]/1.0)))
 pp=np.c_[[np.interp(u,s,p[:,i]) for i in range(3)]].T
 worst=[];closestall=(float('inf'),None,None)
 for idx,q in enumerate(pp):
  best=(float('inf'),None)
  for obj,field in fields.items():
   lo,hi=bounds[obj]
   bb_dist=np.linalg.norm(np.maximum(np.maximum(lo-q,q-hi),0))
   if bb_dist>max(7.,best[0]+5):continue
   dist=abs(field.EvaluateFunction(q))-5.
   if dist<best[0]:best=(dist,obj)
  if best[0]<closestall[0]:closestall=(best[0],best[1],q.tolist())
  if best[0]<-.20:worst.append({'station_mm':float(u[idx]),'penetration_mm':float(-best[0]),'object':best[1],'center_mm':q.tolist()})
 hits.extend([{'path':name,**h} for h in worst])
 reports.append({'path':name,'length_mm':float(s[-1]),'max_rise_between_samples_mm':float(np.diff(p[:,2]).max()),'minimum_surface_clearance_mm':float(closestall[0]),'closest_object':closestall[1],'closest_center_mm':closestall[2],'sample_count':len(pp),'samples_below_minus_0_2mm':len(worst),'worst_samples':sorted(worst,key=lambda x:x['penetration_mm'],reverse=True)[:5]})
 print('CLEARANCE',name,'min',round(closestall[0],3),'hits',len(worst),'obj',closestall[1],flush=True)
(ROOT/'Checks/Sampled_clearance_report.json').write_text(json.dumps({'description':'Unsigned tessellated-surface sphere clearance, 10mm marble, <=1mm nominal station interval. Peg board intentionally interrupts travel, so not checked as a straight trajectory. No dynamic/print/strength validation.','tracks':reports,'penetrations_over_0_2mm':hits},indent=2))
print('CHECKS_DONE',flush=True)
