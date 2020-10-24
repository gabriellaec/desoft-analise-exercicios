def calcula_tempo(acc):
    import math as m
    t = dict()
    for n, a in acc.items():
        t[n] = m.sqrt(200/a)
    return t