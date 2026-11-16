import json,os,urllib.request as W;U=os.getenv("MAKEFUN_ENV_URL")
VL=[0,100,320,330,500,900,0]
PS='LLLLLLQQLLV[LQ[eV[ejejoty~~~LLLL$38=3BLL=LV[BQ[`BQ[`=LV[3BLL$38==BBGBQLLGLQVGQVVGQVVGLQVBLLL=BBGLLQVLLLLLLLLLLLLLLLLLLLLQVVVLLQV=BGLBLLLGLQQLLQQLLQQGLQQBLLL=BGL[eLBQVL=B==8=33.8..)3))$3))$3))$'
FL="abcdefgh"
TB=[None]+[[ord(PS[p*32+(i>>3)*4+min(i&7,7-(i&7))])-76 for i in range(64)]for p in range(6)]
KN=[31,33,14,18,-14,-18,-31,-33];K8=[16,-16,1,-1,17,15,-15,-17]
OR=K8[:4]
CM={0:13,7:14,4:12,112:7,119:11,116:3}
F=10**7;B=[0]*144;S=1;C=0;EP=-1;N=0;NB=72000;TT={};X=Exception
def po(p,b):
 q=W.Request(U+p,data=json.dumps(b).encode())
 with W.urlopen(q)as r:return json.load(r)
def atk(s,by):
 if by in(B[s-16*by-1],B[s-16*by+1]):return 1
 for ds,t in((KN,2),(K8,6)):
  for d in ds:
   x=s+d
   if not x&136 and B[x]==t*by:return 1
 for d in K8:
  x=s;t=3+(d in OR)
  while 1:
   x+=d
   if x&136:break
   p=B[x]
   if p:
    if p==by*t or p==by*5:return 1
    break
 return 0
def gen(cap=0):
 ms=[]
 for s in range(128):
  p=B[s]if not s&136 else 0
  if p*S<=0:continue
  t=abs(p)
  if t==1:
   d=16*S;xs=(5,4,2,3)if(s>>4)==(1+5*(S>0))else(0,)
   for df in(-1,1):
    to=s+d+df
    if not to&136 and(B[to]*S<0 or to==EP):ms+=[s|to<<7|x<<14 for x in xs]
   to=s+d
   if not B[to]and(not cap or len(xs)>1):
    ms+=[s|to<<7|x<<14 for x in xs]
    if len(xs)==1 and(s>>4)==(6-5*(S>0))and not B[s+2*d]:ms.append(s|(s+2*d)<<7)
  else:
   for d in(KN if t==2 else K8[4:]if t==3 else OR if t==4 else K8):
    to=s
    for _ in range(8):
     to+=d
     if to&136:break
     if B[to]*S<=0 and(not cap or B[to]):ms.append(s|to<<7)
     if B[to]or t in(2,6):break
   if t==6 and not cap:
    kf=60-56*S;bb=(5-3*S)//2
    for bit,sg in((bb,1),(bb*2,-1)):
     if s==kf and C&bit and not any(B[e]for e in(kf+sg,kf+2*sg)+((),(kf+3*sg,))[sg<0])and not any(atk(x,-S)for x in(kf,kf+sg,kf+2*sg)):ms.append(s|(kf+2*sg)<<7)
 return ms
def mk(m):
 global S,C,EP
 f,t,pr=m&127,(m>>7)&127,m>>14;p=B[f]
 if t==EP and abs(p)==1:B[t-16*S]=0
 B[t]=pr*S if pr else p;B[f]=0
 if(t-f)in(2,-2)and abs(p)>5:
  rf,rt=(f+3,f+1)if t>f else(f-4,f-1);B[rt]=B[rf];B[rf]=0
 C&=CM.get(f,15)&CM.get(t,15);EP=(f+t)//2 if abs(p)==1 and(t-f)in(32,-32)else-1;S=-S
def od(ms,tm):
 ms.sort(key=lambda m:(1<<24)if m==tm else(1<<20)+VL[abs(B[(m>>7)&127])]if B[(m>>7)&127]or m>>14 else 0,reverse=True);return ms
def sr(d,a,b):
 global N,B,S,C,EP
 N+=1
 if N>NB:raise X
 inc=atk(B.index(6*S),-S);q=d<=0 and not inc
 if q:
  st=0
  for j in range(64):
   p=B[(j>>3)*16+(j&7)]
   if p:
    t=abs(p);v=VL[t]+TB[t][j if p>0 else j^56];st+=v if p>0 else-v
  st*=S
  if st>=b:return b
  a=max(a,st)
 ent=TT.get((tuple(B),S,C,EP))if d>0 else None
 tm=ent[2]if ent else-1
 if ent and ent[0]>=d:return ent[1]
 best=-F;bm=-1
 for m in od(gen(q),tm):
  w=(B[:],S,C,EP);mk(m)
  if atk(B.index(-6*S),S):B,S,C,EP=w;continue
  v=-sr(d-1,-b,-a);B,S,C,EP=w
  if v>best:best,bm=v,m
  if v>a:a=v
  if a>=b:break
 if bm<0:return-100000 if inc else a if d<=0 else 0
 if d>0:TT[(tuple(B),S,C,EP)]=(d,best,bm)
 return best
def ch(fen):
 global B,S,C,EP,N
 ps=fen.split();bd=[0]*144
 for i,row in enumerate(ps[0].split('/')):
  r=7-i;f=0
  for ch in row:
   if ch.isdigit():f+=int(ch)
   else:v="pnbrqk".index(ch.lower())+1;bd[r*16+f]=v if ch.isupper()else-v;f+=1
 B=bd;S=1 if ps[1]=='w'else-1
 C=sum(1<<i for i,c in enumerate("KQkq")if c in ps[2])
 EP=-1 if ps[3]=='-'else ord(ps[3][0])-97+16*(int(ps[3][1])-1)
 TT.clear();N=0;legal=[]
 for m in gen():
  w=(B[:],S,C,EP);mk(m)
  if not atk(B.index(-6*S),S):legal.append(m)
  B,S,C,EP=w
 best=legal[0]
 try:
  for d in range(40):
   a=-F;bm=best
   for m in od(legal[:],best):
    w=(B[:],S,C,EP);mk(m);v=-sr(d-1,-F,-a);B,S,C,EP=w
    if v>a:a,bm=v,m
   best=bm
   if N>NB:break
 except X:pass
 f,t,pr=best&127,(best>>7)&127,best>>14
 return FL[f&7]+str((f>>4)+1)+FL[t&7]+str((t>>4)+1)+("  nbrq"[pr]if pr else"")
while 1:
 g=po("/game",{})
 if g["status"]=="done":break
 while g["status"]=="your_move":
  mv=ch(g["fen"])
  g=po("/move",{"game":g["game"],"move":mv if mv in g["legal_moves"]else g["legal_moves"][0]})
