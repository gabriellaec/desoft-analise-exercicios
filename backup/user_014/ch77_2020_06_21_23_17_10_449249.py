import math

def calcula_tempo(atletas):
    tempos = {}
    for nome, aceleracao in atletas.items():
        a_para_t = aceleracao
        t = math.sqrt(200 * a_para_t)
        tempos[nome] = t