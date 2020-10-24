import math
def calcula_tempo(x):
    y={}
    for k,v in x.items():
        tempo=math.sqrt((100*2)/v)
        y[k]=tempo
    return y