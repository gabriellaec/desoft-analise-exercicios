import math

def calcula_tempo(atletas):
    tempos = {}
    for nome, aceleracao in atletas.items():
        t = math.sqrt(200/aceleracao)
        tempos[nome] = t
    return tempos