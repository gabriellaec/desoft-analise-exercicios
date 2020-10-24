import math
def calcula_tempo(dicio):
    v=list(dicio.values())
    d=[0]*len(v)
    for i in v:
        d[i]=math.sqrt(200/v[i])
    return d
