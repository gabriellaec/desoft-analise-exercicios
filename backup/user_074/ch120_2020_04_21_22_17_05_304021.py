import random
d=100
print(d)
v=int(input('valor da aposta:'))
while v>0 and d>0 and v<=d:
    a=input('aposta entre p e n')
    if a==n:
        rr=random.randint(1,36)
        r=int(input('numero entre 1 e 36'))
        if rr==r:
            d=v*35+d
            print(d)
        else:
            if v!=d:
                d=d-v
                print(d)
            else:
                d=0
                print(d)
                break
    else:
        pi=input('impar(i) ou par(p)?')
        s=random.randint(0,36)
        if p==pi:
            if s%2==0:
                d=d+v
                print(d)
            else:
                d=d-v
                print(d)
        else:
            if p%2!=0:
                d=d+v
                print(d)
            else:
                d=d-v
                print(d)
    if d==0:
        print('sem dinheiro')
        break
    else:
        v=int(input('valor da aposta')
        print(d)

            
        
    