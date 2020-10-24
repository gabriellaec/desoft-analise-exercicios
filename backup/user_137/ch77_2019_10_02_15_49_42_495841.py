def calcula_tempo(d):
    for i in d:
        d[i] = 100/int(d[i])
    return d