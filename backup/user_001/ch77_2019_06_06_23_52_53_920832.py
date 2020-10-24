def calcula_tempo(dic_a):
    dic_t = {}
    for k,a in dic_a.items():
        if a <= 0:
            t = -1
        else:
            t = (200/a)**0.5
        dic_t[k] = t