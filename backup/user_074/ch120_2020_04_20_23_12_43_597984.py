import random
d=100
print(d)
v=int(input('valor da aposta:'))
while v>0 and d>0:
    a=input('aposta' n/p)
    if d==0:
        break
    if a==n:
        rr=random.randint(1,36)
        r=int(input('numero entre 1 e 36'))
        if rr==r:
            d=v*35+d
        else:
            d=d-v
    else:
        pi=input('impar ou par?'i/p)
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
    print(d)

            
        
    