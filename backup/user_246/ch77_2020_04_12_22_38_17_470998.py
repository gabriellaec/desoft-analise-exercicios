import math
def calcula_tempo(alt):
    lnome=list(alt.keys())
    lacel=list(alt.values())
    ltem=[]
    for i in lacel:
        v=math.sqrt(200/i)
        ltem.append(v)
    t=0
    for i in lnome:
        alt[i]=ltem[t]
        t+=1
    return alt
        
    