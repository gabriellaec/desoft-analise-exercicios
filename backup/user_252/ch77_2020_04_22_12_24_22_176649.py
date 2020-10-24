import math
def calcula_tempo(x):
    y={}
    for k,v in x.items():
        t=math.sqrt((100*2)/v)
        y[k]=t
    return y