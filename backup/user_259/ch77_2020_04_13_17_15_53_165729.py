from math import sqrt
def calcula_tempo(dic):
    tempos = {}
    for i in dic:
        tempo = sqrt(200/dic[i])
        tempos[i] = tempo
    return tempos
