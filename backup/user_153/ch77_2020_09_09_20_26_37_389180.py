def calcula_tempo(dic):
    tempos = {}
    for key, value in dic.items():
        tempos[key] = (200/value)**0.5
    return tempos
        