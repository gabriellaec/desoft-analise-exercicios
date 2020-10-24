import math
def calcula_tempo(d):
    r = {}
    for i,a in d.items():
        t = math.sqrt((100*2)/a)
        r[i] = t 
    return r