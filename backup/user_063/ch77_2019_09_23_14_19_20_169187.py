import math
def calcula_tempo(dicionario):
    s = 100
    a = dicionario.values()
    t = math.sqrt(2*s/a)
    dados_corredores = {}
    for x in dicionario:
        dados_corredores[x] = t
    return dados_corredores