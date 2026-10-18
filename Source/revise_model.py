"""Revise the approved photo reconstruction, preserving its existing layout.
Assistant-generated prototype, estimated dimensions; no claim of physical testing.
"""
from pathlib import Path
import cadquery as cq
import numpy as np
from scipy.interpolate import CubicSpline,PchipInterpolator
import json, math, shutil, time
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT.parent/'Marble_Mayhem_Photo_Rebuild'
if not (SRC/'Checks/Components.json').exists():
 import zipfile
 SRC=ROOT/'Source/Input_Approved_Model'
 with zipfile.ZipFile(ROOT/'Source/Input_Approved_Model.zip') as z:z.extractall(SRC)
C={'black':(.075,.080,.085),'blue':(.025,.13,.69),'orange':(1.,.30,.018),'green':(.24,.82,.035),'silver':(.68,.72,.77),'clear':(.66,.80,.88)}
for d in ['CAD/Components','STL_Prototype','Checks','Checks/mesh_cache','Source']:(ROOT/d).mkdir(parents=True,exist_ok=True)
info=json.loads((SRC/'Checks/Components.json').read_text())
paths={k:np.array(v,float) for k,v in json.loads((SRC/'Checks/Nominal_marble_paths.json').read_text()).items()}
items={}
def V(p):return cq.Vector(*map(float,p))
def box(c,d):return cq.Workplane('XY').box(*d).translate(tuple(c)).val()
def cyl(p,r,h):return cq.Solid.makeCylinder(r,h,V(p),V((0,0,1)))
def bar(a,b,r):
 a,b=V(a),V(b);v=b-a
 return cq.Solid.makeCylinder(r,v.Length,a,v.normalized())
def frames(p):
 p=np.array(p,float);t=np.gradient(p,axis=0);t/=np.linalg.norm(t,axis=1)[:,None]
 n=np.c_[-t[:,1],t[:,0],np.zeros(len(t))];n/=np.linalg.norm(n,axis=1)[:,None]
 up=np.cross(t,n);up/=np.linalg.norm(up,axis=1)[:,None]
 return t,n,up
def smooth(ctrl,N=70,startdir=None,enddir=None):
 q=np.array(ctrl,float);s=np.r_[0,np.cumsum(np.linalg.norm(np.diff(q,axis=0),axis=1))];u=np.linspace(0,s[-1],N)
 a=np.array(q[1]-q[0] if startdir is None else startdir,float);a/=np.linalg.norm(a)
 b=np.array(q[-1]-q[-2] if enddir is None else enddir,float);b/=np.linalg.norm(b)
 xy=CubicSpline(s,q[:,:2],bc_type=((1,a[:2]),(1,b[:2])))(u)
 z=PchipInterpolator(s,q[:,2])(u)
 return np.c_[xy,z]
def tube(p,r):
 p=np.array(p);e=cq.Edge.makeSpline([V(a) for a in p],tol=1e-5);w=cq.Wire.assembleEdges([e])
 profile=cq.Wire.makeCircle(r,V(p[0]),e.tangentAt(0))
 s=cq.Solid.sweep(profile,[],w,True,False)
 if not s.isValid():raise RuntimeError('Invalid swept tube')
 return s
def loftpoly(p,poly):
 p=np.array(p);_,nn,uu=frames(p);w=[]
 for a,n,u in zip(p,nn,uu):
  pts=[V(a+x*n+y*u) for x,y in poly];w.append(cq.Wire.makePolygon(pts+[pts[0]]))
 s=cq.Solid.makeLoft(w,False)
 if not s.isValid():raise RuntimeError('Invalid loft')
 return s
def channel(p,width=14.4,wall=7.,thick=1.8):
 w=width/2
 return loftpoly(p,[(-w-thick,-5.4-thick),(w+thick,-5.4-thick),(w+thick,wall),(w,wall),(w,-5.4),(-w,-5.4),(-w,wall),(-w-thick,wall)])
def cavity(p,w=7.2):return loftpoly(p,[(-w,-5.35),(w,-5.35),(w,14),(-w,14)])
def rails(p,count=10,r=1.6):
 p=np.array(p);_,n,up=frames(p)
 ss=[tube(p-5.2*n-4.3*up,r),tube(p+5.2*n-4.3*up,r)]
 for j in np.unique(np.linspace(0,len(p)-1,count,dtype=int)):
  c=p[j]-6.7*up[j];ss.append(bar(c-6.5*n[j],c+6.5*n[j],1.4))
 return cq.Compound.makeCompound(ss)
def put(name,s,col,group='New_features',printable=True,changed=True):
 if not s.isValid():raise RuntimeError('Invalid '+name)
 if len(s.Solids())==0:raise RuntimeError('No solids '+name)
 items[name]={'name':name,'shape':s,'col':col,'group':group,'printable':printable,'changed':changed}
 print('READY',name,'solids',len(s.Solids()),'volume',round(s.Volume(),1),flush=True)
 return s
def readpart(name):return cq.importers.importStep(str(SRC/'CAD/Components'/(name+'.step'))).val()
for it in info:
 s=readpart(it['name']);put(it['name'],s,it['col'],it['group'],it['printable'],False)
print('LOADED original',len(items),flush=True)

# CHANGE 1: Extend the open loader by the orange ladder to the existing funnel.
# The loader is the local high point: both selectable directions run DOWNHILL.
a1=paths['07_Green_upper_snaking_rails'];t1,n1,u1=frames(a1)
bridge=smooth([tuple(a1[0]),(-101,86,169.6),(-102,98,169.0),(-86,102,168),(-55,102,165.4),(-20,102,162.7),(18,103,159.5),(44,102,157),(59,99,154),(64,88,141.8)],125,startdir=(-1,.12,-.03),enddir=(0,-1,-.8))
# Paired green rails retain the look of the approved model; final channel captures the bowl.
k=103
bridge_rails=rails(bridge[:k+1],20)
put('30_Green_ladder_to_funnel_bridge',bridge_rails,'green','Funnel_link')
bridge_mouth=channel(bridge[k:],width=15.,wall=5.2,thick=1.8)
put('31_Green_funnel_entry_chute',bridge_mouth,'green','Funnel_link')
paths['30_Ladder_to_funnel_bridge']=bridge
# Saddle joins the two previously open rail ends at the common loading ridge.
pos=a1[0];t=t1[0];n=n1[0];up=u1[0]
prof=[(-8.8,-9),(8.8,-9),(8.8,-4.8),(7,-4.8),(7,-7.1),(-7,-7.1),(-7,-4.8),(-8.8,-4.8)]
pts=[V(pos+x*n+y*up-t*4) for x,y in prof];wire=cq.Wire.makePolygon(pts+[pts[0]])
put('32_Blue_loader_join_saddle',cq.Solid.extrudeLinear(wire,[],V(t*8)),'blue','Joints')
# Existing rear ladder tops are relieved ONLY where the new ball envelope passes.
bridge_clear=tube(bridge,5.45)
for name in ['23_Orange_rear_ladder_0','23_Orange_rear_ladder_1']:
 s=items[name]['shape'].cut(bridge_clear)
 put(name,s,items[name]['col'],'Supports')
# Final chute is trimmed against the bowl's solid skin if necessary, while keeping a clear entry.
bowl=items['02_Orange_funnel']['shape']
# A nominal 10.9 mm passage through a rim that would otherwise obstruct the marble.
bowl2=bowl.cut(bridge_clear)
put('02_Orange_funnel',bowl2,'orange','Funnel')
# Supports behind the layout; all feet remain on the original base.
for i,(idx,basepoint) in enumerate([(28,(-76,98,4)),(65,(-6,98,4)),(96,(48,96,4))],1):
 p=bridge[idx];_,_,up=frames(bridge);q=p-8.4*up[idx]
 b=np.array(basepoint,float);top=np.array([b[0],b[1],q[2]])
 ss=[cyl(b,2.6,q[2]-4),cyl(b,4.8,2.0),bar(top,q,2.0)]
 # Two actual tie bars meet the track supports, not arbitrary floating poles.
 _,nn,uu=frames(bridge);c=p-6.7*uu[idx];ss.append(bar(c-6.5*nn[idx],c+6.5*nn[idx],1.4))
 put('33_Orange_bridge_post_'+str(i),cq.Compound.makeCompound(ss),'orange','Supports')

# CHANGE 2: A genuine fork in the upper return, with an alternate Plinko course.
main=paths['09_Green_return_to_steps']
# Replace only the first 21 path samples by a three-way open junction.
cutidx=15
originaltail=rails(main[cutidx:],9)
put('09_Green_return_to_steps',originaltail,'green','Tracks')
angle=math.radians(35);d=np.array([0,-math.cos(angle),-math.sin(angle)]);up=np.array([0,-math.sin(angle),math.cos(angle)]);xx=np.array([-1.,0,0])
entry=np.array([-50.,-12.,105.])
# A planar T/Y selector is robust CAD: open shared floor, two outlets, no intersecting walls.
t0,n0,u0=frames(main[:16]);t0,n0,u0=t0[0],n0[0],u0[0]
length=float(np.linalg.norm(main[15]-main[0]));origin0=main[0]-5.4*u0
plane0=cq.Plane(origin=V(origin0),xDir=V(t0),normal=V(u0))
outline0=[(0,-9),(length,-9),(length,9),(23,9),(23,18),(5,18),(5,9),(0,9)]
fork=cq.Workplane(plane0).polyline(outline0).close().extrude(-1.8).val()
# Wall strips; ports at u=0, u=length and v=18 remain open.
for center,dims in [((length/2,-8.1),(length,1.8)),((2.5,8.1),(5,1.8)),(((length+23)/2,8.1),(length-23,1.8)),((5.9,13.05),(1.8,9.9)),((22.1,13.05),(1.8,9.9))]:
 wall=cq.Workplane(plane0).center(*center).rect(*dims).extrude(12).val();fork=fork.fuse(wall)
put('34a_Green_two_way_route_selector',fork.clean(),'green','Plinko_route')
feedstart=main[0]+14*t0+18*n0
feed=smooth([tuple(feedstart),(-38.0,6,133.5),(-45,-1,125),(-50,-4,113),(-50,-8,107.8),tuple(entry)],66,startdir=(0,-1,-.05),enddir=d)
put('34b_Green_selector_to_Plinko_chute',channel(feed,width=14.4,wall=7.0),'green','Plinko_route')
paths['34_Plinko_inlet_chute']=feed
# Main selector remains on the exact original main route.
# An alternate path through its floor is a geometric route choice, not a kinematic result.
selector_path=np.array([main[0],main[0]+8*t0,main[0]+14*t0+7*n0,feedstart])
paths['34a_Selector_branch']=selector_path
# Local board y axis points downhill; X is perpendicular to travel.
origin=entry-5.4*up
plane=cq.Plane(origin=V(origin),xDir=V(xx),normal=V(up))
L=80.0
outline=[(-33,-5),(33,-5),(33,60),(9.2,L),(-9.2,L),(-33,60)]
floor=cq.Workplane(plane).polyline(outline).close().extrude(-2.2).val()
# Four staggered peg rows, with 15.4 mm between neighboring pegs in a row.
pegcoords=[]
for row,s in enumerate([12.,27.,42.,57.]):
 for x in ([-19.,0.,19.] if row%2==0 else [-9.5,9.5]):
  pegcoords.append((x,s))
  peg=cq.Solid.makeCylinder(1.8,10,V(origin+xx*x+d*s),V(up))
  floor=floor.fuse(peg)
# Under-deck longitudinal stiffeners.
for x in [-20,20]:
 points=[(-1,0),(1,0),(1,57),(-1,57)]
 rib=cq.Workplane(plane).center(x,0).polyline(points).close().extrude(-4.0).val();floor=floor.fuse(rib)
put('35_Orange_Plinko_board_with_pegs',floor.clean(),'orange','Plinko_route')
# Blue sidewalls taper toward the outlet. Keep the inlet and outlet OPEN.
wall_shapes=[]
def planar_wall(a,b,w=1.8,h=12):
 a=np.array(a,float);b=np.array(b,float);v=b-a;n=np.array([-v[1],v[0]]);n/=np.linalg.norm(n)
 pts=[a-n*w/2,b-n*w/2,b+n*w/2,a+n*w/2]
 return cq.Workplane(plane).polyline([tuple(p) for p in pts]).close().extrude(h).val()
for a,b in [((-32.1,-5),(-32.1,59.6)),((-32.1,59.6),(-8.3,L)),((32.1,-5),(32.1,59.6)),((32.1,59.6),(8.3,L)),((-32.1,-4.1),(-8.3,-4.1)),((8.3,-4.1),(32.1,-4.1))]:wall_shapes.append(planar_wall(a,b))
put('36_Blue_Plinko_sidewalls',cq.Compound.makeCompound(wall_shapes),'blue','Plinko_route')
exitpoint=entry+d*L
out=smooth([tuple(exitpoint),(-48,-83,45),(-32,-96,32),(-10,-100,24),(22,-98,19)],80,startdir=d,enddir=(1,.10,-.10))
outshape=channel(out,width=14.4,wall=6.,thick=1.8)
# Clearance opening where the existing lower return enters the common catcher.
oldlow=paths['12_Green_lower_wave_return'];oldtan=oldlow[-1]-oldlow[-2];oldtan/=np.linalg.norm(oldtan)
cutpass=tube(oldlow[-18:],5.55)
cutpass=cutpass.fuse(cq.Solid.makeCylinder(5.55,18,V(oldlow[-1]),V(oldtan)))
outshape=outshape.cut(cutpass)
put('37_Green_Plinko_return_to_catcher',outshape,'green','Plinko_route')
paths['37_Plinko_return_to_catcher']=out
# Straight corridor through the board is NOT used as a validation claim; pegs intentionally interrupt it.
(ROOT/'Checks/Plinko_design.json').write_text(json.dumps({'inlet_marble_center_mm':entry.tolist(),'outlet_marble_center_mm':exitpoint.tolist(),'slope_degrees':35,'peg_radius_mm':1.8,'row_pitch_mm':15,'horizontal_pitch_mm':19,'minimum_same_row_gap_mm':15.4,'nominal_marble_diameter_mm':10,'peg_centers_local_mm':pegcoords,'note':'Peg collisions and alternate paths are deliberate. Physical bounce/jam testing required.'},indent=2))
# Four pillars offset if needed to keep the existing low marble return unobstructed.
allp=np.vstack(list(paths.values()))
for i,(x,s) in enumerate([(-25,9),(25,9),(-12,69),(12,69)],1):
 target=origin+xx*x+d*s-3.2*up
 chosen=None
 for dx,dy in [(0,0),(12,0),(-12,0),(0,12),(0,-12),(18,0),(-18,0),(15,10),(-15,10)]:
  q=target+np.array([dx,dy,0.])
  zclip=np.clip(allp[:,2],4,q[2]);dist=np.linalg.norm(allp-np.c_[np.full(len(allp),q[0]),np.full(len(allp),q[1]),zclip],axis=1)
  if dist.min()<8.3:continue
  vec=target-q
  if np.linalg.norm(vec)>1.e-6:
   lam=np.clip((allp-q)@vec/(vec@vec),0,1)
   if np.linalg.norm(allp-q-lam[:,None]*vec,axis=1).min()<8.0:continue
  chosen=q;break
 if chosen is None:raise RuntimeError('No clear location for Plinko post '+str(i))
 q=chosen
 ss=[cyl((q[0],q[1],4),2.6,q[2]-4),cyl((q[0],q[1],4),4.5,2),cq.Solid.makeSphere(3.3,V(target),angleDegrees1=-90,angleDegrees2=90)]
 if np.linalg.norm(q-target)>1.e-6:ss.append(bar(q,target,2.6))
 put('38_Blue_Plinko_support_'+str(i),cq.Compound.makeCompound(ss),'blue','Supports')
# A separate small support for the descending exit.
j=30;p=out[j];_,_,u=frames(out);target=p-8.1*u[j]
put('39_Green_Plinko_exit_support',cyl((target[0],target[1],4),2.5,target[2]-4).fuse(cyl((target[0],target[1],4),4.5,2)),'green','Supports')

# CHANGE 3: A slim central tower INSIDE the existing shrinking spiral.
# Its outer radius leaves space for the innermost 10mm-marble trajectory.
coil=paths['05_Green_front_vortex'];_,n,u=frames(coil)
column=cyl((32,-38,4),3.2,88).cut(cyl((32,-38,4),1.4,86))
column=column.fuse(cyl((32,-38,4),7.,2.5))
spoke_indices=[26,97,168,230]
for j in spoke_indices:
 target=coil[j]-8.4*u[j];start=np.array([32.,-38.,target[2]])
 arm=bar(start,target,1.8)
 c=coil[j]-6.7*u[j];tie=bar(c-6.5*n[j],c+6.5*n[j],1.4)
 column=column.fuse(arm).fuse(tie)
put('40_Orange_central_spiral_column_and_arms',column,'orange','Spiral_support')

# A collision-free, monotonically downhill example corridor through the pegs.
# This is a geometric path, not a prediction of how bouncing marbles actually travel.
qgrid=np.arange(-27.,27.01,.5);sgrid=np.arange(0.,L+.01,.5)
parents=[];cost=np.full(len(qgrid),float('inf'));cost[np.argmin(abs(qgrid))]=0.
for ri,ss0 in enumerate(sgrid):
 half=31.2 if ss0<=60 else 31.2-(31.2-7.4)*(ss0-60)/(L-60)
 allowed=abs(qgrid)<=half-5.15
 # Stay in the inlet throat until the ball has cleared the feed chute's end walls.
 allowed &= abs(qgrid)<=max(0,1.7*(ss0-3.5))
 for q0,s0 in pegcoords:allowed &= (qgrid-q0)**2+(ss0-s0)**2>=(7.0)**2
 newcost=np.full(len(qgrid),float('inf'));par=np.full(len(qgrid),-1,int)
 for j0 in np.where(allowed)[0]:
  options=[j for j in range(max(0,j0-3),min(len(qgrid),j0+4)) if np.isfinite(cost[j])]
  if options:
   j=min(options,key=lambda j:cost[j]+.2*(qgrid[j]-qgrid[j0])**2)
   newcost[j0]=cost[j]+qgrid[j0]**2+.2*(qgrid[j]-qgrid[j0])**2;par[j0]=j
 if not np.isfinite(newcost).any():raise RuntimeError('No geometric Plinko corridor')
 cost=newcost;parents.append(par)
j=min(np.where(np.isfinite(cost))[0],key=lambda j:cost[j]+1000*qgrid[j]**2);qs=[]
for par in parents[::-1]:qs.append(qgrid[j]);j=par[j]
qs=qs[::-1]
boardpath=np.array([entry+xx*q+d*ss0 for q,ss0 in zip(qs,sgrid)])
paths['35_Example_Plinko_clear_corridor_NOT_dynamics']=boardpath
put('DISPLAY_Plinko_ball',cq.Solid.makeSphere(5,V(boardpath[76]),angleDegrees1=-90,angleDegrees2=90),'silver','Display_balls',False)
# Added display ball in the new bridge (not a printed part).
p=bridge[74]
put('DISPLAY_new_bridge_ball',cq.Solid.makeSphere(5,V(p),angleDegrees1=-90,angleDegrees2=90),'silver','Display_balls',False)

# Record checks and export real CAD, keeping unchanged geometry from the approved file.
(ROOT/'Checks/Nominal_marble_paths.json').write_text(json.dumps({k:v.tolist() for k,v in paths.items()},indent=2))
newjoins=[{'name':'Ladder loading ridge to funnel bridge','a':'07_Green_upper_snaking_rails','ia':0,'b':'30_Ladder_to_funnel_bridge','ib':0},
 {'name':'Scoop to new route fork','a':'08_Orange_transfer_scoop','ia':-1,'b':'34a_Selector_branch','ib':0}]
newjoins.append({'name':'Selector to Plinko feed','gap_mm':float(np.linalg.norm(selector_path[-1]-feed[0]))})
newjoins.append({'name':'Plinko inlet','gap_mm':float(np.linalg.norm(feed[-1]-entry))})
newjoins.append({'name':'Plinko outlet','gap_mm':float(np.linalg.norm(out[0]-exitpoint))})
for j in newjoins:
 if 'a' in j:j['gap_mm']=float(np.linalg.norm(paths[j['a']][j['ia']]-paths[j['b']][j['ib']]))
(ROOT/'Checks/New_joint_positions.json').write_text(json.dumps(newjoins,indent=2))
assembly=cq.Assembly(name='Marble_Mayhem_V2_Funnel_Link_Plinko_Column')
summary=[]
for it in items.values():
 name=it['name'];s=it['shape'];col=it['col'];assembly.add(s,name=name,color=cq.Color(*C[col],.45 if col=='clear' else 1))
 dst=ROOT/'CAD/Components'/(name+'.step')
 if not it['changed']:shutil.copy2(SRC/'CAD/Components'/(name+'.step'),dst)
 else:cq.exporters.export(s,str(dst))
 if it['printable']:
  stldst=ROOT/'STL_Prototype'/(name+'.stl')
  srcstl=SRC/'STL_Prototype'/(name+'.stl')
  if not it['changed'] and srcstl.exists():shutil.copy2(srcstl,stldst)
  else:cq.exporters.export(s,str(stldst),tolerance=.10,angularTolerance=.20)
 verts,faces=s.tessellate(.12,.22)
 vv=np.array([[v.x,v.y,v.z] for v in verts]);ff=np.array(faces)
 np.savez_compressed(ROOT/'Checks/mesh_cache'/(name+'.npz'),vertices=vv,faces=ff)
 bb=s.BoundingBox()
 summary.append({k:it[k] for k in ['name','col','group','printable','changed']}|{'valid':s.isValid(),'solid_count':len(s.Solids()),'volume_mm3':s.Volume(),'bounds_mm':[bb.xmin,bb.xmax,bb.ymin,bb.ymax,bb.zmin,bb.zmax]})
 print('EXPORTED',name,flush=True)
(ROOT/'Checks/Components.json').write_text(json.dumps(summary,indent=2))
assembly.export(str(ROOT/'CAD/Marble_Mayhem_V2_assembled.step'))
print('EXPORTED ASSEMBLY',len(items),flush=True)
