def calcula_tempo(dic):
    tempos = {}
    for i in dic:
        tempo = (200/dic[i])**0.5
        tempo[i] = tempo
    return tempos
    