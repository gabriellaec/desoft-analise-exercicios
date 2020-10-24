import math
def calcula_tempo(dicionario):
    dicionario2={}
    for i in dicionario:
        dicionario2[i]=math.sqrt(200/dicionario[i])

    return dicionario2