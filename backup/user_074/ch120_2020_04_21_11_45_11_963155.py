import random
d=100
p=str
n=str
i=str
print(d)
v=int(input('valor da aposta:'))
while v>0 and d>0:
    a=input('aposta entre {} e {}'.format(p,n))
    if a==n:
        rr=random.randint(1,36)
        r=int(input('numero entre 1 e 36'))
        if rr==r:
            d=v*35+d
        else:
            if v!=d:
                d=d-v
            else:
                d=0
                break
    else:
        pi=input('impar{} ou par{}?'.format(i,p))
        s=random.randint(0,36)
        if p==pi:
            if s%2==0:
                d=d+v
            else:
                d=d-v
        else:
            if p%2!=0:
                d=d+v
            else:
                d=d-v
    if d==0:
        break
    else:
        v=int(input('valor da aposta')
    print(d)

            
        
    