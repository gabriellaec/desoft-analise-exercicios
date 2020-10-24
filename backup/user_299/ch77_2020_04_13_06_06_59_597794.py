import math

def calcula_tempo(dicio):
    corredores = {}
    for nome, ace in dicio.items():
        t = math.sqrt(200/ace)
        corredores[nome] = t
    return corredores