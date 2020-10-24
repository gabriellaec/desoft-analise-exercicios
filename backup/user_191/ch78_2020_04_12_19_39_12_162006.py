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
    dic[i]=t
print(l)