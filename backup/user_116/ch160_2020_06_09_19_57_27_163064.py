from math import *
listaf=[]
listasin=[]
maior=-1
dicio={}
for values in range(0,91):
    y=sin(values*pi/180)
    x=(4*values*(180-values))/(40500-values*(180-values))
    listaf.append(x)
    listasin.append(y)
for m,n in zip(listasin,listaf):
    if m-n>maior:
        maior=m-n
        dicio[maior]=n

index=listaf.index(dicio[maior])
print(index)
