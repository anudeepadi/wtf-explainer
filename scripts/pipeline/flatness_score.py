import os,sys,json,numpy as np
from PIL import Image
root=sys.argv[1]; out=[]
for n in sorted(d for d in os.listdir(root) if os.path.isdir(os.path.join(root,d))):
    d=os.path.join(root,n)
    for f in sorted(x for x in os.listdir(d) if x.endswith('.jpg') and not x.startswith('._')):
        im=np.asarray(Image.open(os.path.join(d,f)).convert('RGB').resize((160,90)),dtype=np.int16)
        q=(im//32).reshape(-1,3); keys=q[:,0]*64+q[:,1]*8+q[:,2]
        cnt=np.bincount(keys,minlength=512); top=np.sort(cnt)[::-1]
        dom=top[0]/keys.size; top3=top[:3].sum()/keys.size
        g=np.abs(np.diff(im.mean(2),axis=1)).mean()
        hsv=np.asarray(Image.fromarray(im.astype(np.uint8)).convert('HSV'),dtype=np.int16)
        idx=int(f[2:7]); out.append((n,idx,round(dom,3),round(top3,3),round(float(g),2),round(float(hsv[...,1].mean()),1)))
json.dump(out,open(sys.argv[2],'w'))
