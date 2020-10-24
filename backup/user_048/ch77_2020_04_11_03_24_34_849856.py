import math
def calcula_tempo(dicio):
    k=dicio.keys()
    v=list(dicio.values())
    d=[0]*len(v)
    for i in range(len(v)):
        d[i]=math.sqrt(200/v[i])
    n=dict(zip(k, d))
    return n
