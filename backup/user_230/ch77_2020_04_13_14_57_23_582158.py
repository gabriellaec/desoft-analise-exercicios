import math as m
def calcula_tempo(atletas):
    dicionario=dict()
    for i in atletas:
        dicionario[i]=m.sqrt(200/atletas[i])
    return dicionario