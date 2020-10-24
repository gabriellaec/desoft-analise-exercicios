import math
v=True
j={}
while v:
    n=input('nome')
    if n=='sair':
        v=False
    else:
        a=float(input('acele'))
        j[n]=a
l={}
for i,u in j.items():
    t=math.sqrt(200/u)
    l[i]=t
v=list(l.values())
k=list(l.keys())
print(k[v.index(max(v))],max(v))