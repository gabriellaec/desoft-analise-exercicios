import math
def calcula_tempo(alt):
    lnome=list(alt.keys())
    lacel=list(alt.values())
    lvel=[]
    for i in lacel:
        v=math.sqnr(200*i)
        lvel.append(v)
    