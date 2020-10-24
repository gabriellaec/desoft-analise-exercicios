import math
def calcula_tempo(alt):
    lnome=list(alt.keys())
    lacel=list(alt.values())
    lvel=[]
    for i in lacel:
        v=math.sqrt(200*i)
        lvel.append(v)
    t=0
    for i in lnome:
        alt[i]=lvel[t]
        t+=1
    return alt
        
    