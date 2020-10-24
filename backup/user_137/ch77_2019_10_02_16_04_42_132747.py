import math

def calcula_tempo(d):
    for i in d:
        d[i] = math.sqrt(2 * 100 / d[i])
    return d