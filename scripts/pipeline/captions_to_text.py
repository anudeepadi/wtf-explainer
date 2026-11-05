import json,sys
src,dst=sys.argv[1],sys.argv[2]
d=json.load(open(src))
out=[];buf=[];start=None;last=0
for e in d.get('events',[]):
    if 'segs' not in e: continue
    t=e.get('tStartMs',0)/1000
    txt=''.join(s.get('utf8','') for s in e['segs']).replace('\n',' ').strip()
    if not txt: continue
    if start is None: start=t
    buf.append(txt)
    if t-start>=20:
        out.append(f"[{int(start//3600):02d}:{int(start%3600//60):02d}:{int(start%60):02d}] "+' '.join(buf)); buf=[];start=None
if buf: out.append(f"[{int(start//3600):02d}:{int(start%3600//60):02d}:{int(start%60):02d}] "+' '.join(buf))
open(dst,'w').write('\n'.join(out))
