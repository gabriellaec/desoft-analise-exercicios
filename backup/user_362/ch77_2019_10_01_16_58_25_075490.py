import math
def calcula_tempo(dicionario):
    tempos = {}
    for i in dicionario:
        tempos[i] = sqrt(200/dicionario[i])
    return tempos

