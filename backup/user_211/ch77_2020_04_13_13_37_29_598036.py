import math
def calcula_tempo(dicionario):
    dic_tempo={}
    for k,v in dicionario.items():
        t= sqrt(200/v)
        dic_tempo[k]=t
    return dic_tempo