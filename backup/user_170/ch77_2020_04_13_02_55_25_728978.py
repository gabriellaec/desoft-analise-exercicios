import math
def calcula_tempo(atletas):
    tConclusao = {}
    for n,a in atletas.items():
        t = math.sqrt(200/a)
        tConclusao[n] = t
    return tConclusao