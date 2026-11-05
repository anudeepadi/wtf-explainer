import os,json,numpy as np
from PIL import Image
res={}
for n in sorted(d for d in os.listdir('frames') if os.path.isdir(os.path.join('frames',d))):
    hits=[]
    for f in sorted(x for x in os.listdir(f'frames/{n}') if x.endswith('.jpg') and not x.startswith('._')):
        im=np.asarray(Image.open(f'frames/{n}/{f}').convert('RGB').resize((192,108)),dtype=np.float32)
        hsv=np.asarray(Image.open(f'frames/{n}/{f}').convert('HSV').resize((192,108)),dtype=np.float32)
        for side,sl in (('R',slice(128,192)),('L',slice(0,64))):
            reg=im[:,sl]; h=hsv[:,sl]
            # panel: mostly one color (median distance small), saturated
            med=np.median(reg.reshape(-1,3),0); dist=np.abs(reg-med).sum(2)
            frac=(dist<60).mean(); sat=h[...,1].mean()
            if frac>0.7 and sat>90: hits.append((int(f[2:7]),side,round(float(frac),2),round(float(sat))))
    res[n]=hits; print(n,len(hits))
json.dump(res,open('panels.json','w'))
