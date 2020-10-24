import math
def calcula_tempo(dicionario):
    dicionario2={}
    for k,v in dicionario.values():
        t=math.sqrt(200/v)
        dicionario2[k]=t
    return dicionario2