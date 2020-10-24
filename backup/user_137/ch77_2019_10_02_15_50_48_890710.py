def calcula_tempo(d):
    for i in d:
        d[i] = int(100/int(d[i]))
    return d