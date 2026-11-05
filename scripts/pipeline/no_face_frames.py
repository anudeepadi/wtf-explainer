import cv2,os,json,sys
cc=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
pc=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_profileface.xml')
res={}
for n in sorted(d for d in os.listdir('frames') if os.path.isdir(os.path.join('frames',d))):
    d=f'frames/{n}'; nf=[]
    for f in sorted(x for x in os.listdir(d) if x.endswith('.jpg') and not x.startswith('._')):
        g=cv2.imread(os.path.join(d,f),0)
        a=cc.detectMultiScale(g,1.15,5,minSize=(24,24)); b=pc.detectMultiScale(g,1.15,5,minSize=(24,24))
        if len(a)==0 and len(b)==0: nf.append(int(f[2:7]))
    res[n]=nf; print(n,len(nf),flush=True)
json.dump(res,open('noface.json','w'))
