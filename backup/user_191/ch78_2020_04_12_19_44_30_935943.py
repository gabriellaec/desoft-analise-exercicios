import math
v=True
l={}
while v:
    n=input('nome')
    if n=='sair':
        v=False
    else:
        a=float(input('acele'))
        l[n]=a
for i,u in l.items():
    t=math.sqrt(200/u)
    l[i]=t
v=list(l.values())
k=list(l.keys())
print(k[v.index(max(v))],max(v))