import math
def bhaskara (ang):
    sen=(4*ang*(180-ang))/(40500-ang*(180-ang))
    return sen
def verifica_maior (dic):
    maior=0
    mang=0
    for ang,n in dic.items():
        if n>maior:
            maior=n
            mang=ang
    return mang  
dif={}
for ang in range (0,91):
    senb=abs(bhaskara(ang))
    senm=abs(math.sin(math.radians(ang)))
    dif[ang]=senb-senm
print (verifica_maior(dif))