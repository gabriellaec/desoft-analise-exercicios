def calcula_tempo (dic):
    dic_f = {}
    for k, a in dic.items():
        t = (200/a)**(1/2)
        dic_f[k] = t
    return dic_f