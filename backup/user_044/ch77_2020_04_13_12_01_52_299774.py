import math
def calcula_tempo(dic):
    dn={}
    for i,n in dic.items():
        t=math.sqrt(200/n)
        dn[i]=t
    return dn