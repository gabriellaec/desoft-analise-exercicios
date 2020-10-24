from math import sqrt
def calcula_tempo(dic):
    tempos = {}
    for i in dic:
        tempo = sqrt(200/dic[i])
        tempo[i] = tempo
    return tempos
print(calcula_tempo({'john': 1.2, 'pedro': 0,9})