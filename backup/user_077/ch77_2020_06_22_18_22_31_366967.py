import math
def calcula_tempo(x):
    resultado={}
    for nome in x:
        a=x[nome]
        t=mat.sqrt(200/a)
        resultado[nome]=t
    return resultado