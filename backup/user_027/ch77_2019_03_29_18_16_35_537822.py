from math import sqrt

def calcula_tempo(x):
    tempos = {}
    for i in x:
        tempos[i] = sqrt(200/x[i])
    return tempos
