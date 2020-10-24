def calcula_tempo(dic_atletas):
    dic = {}
    for k, v in dic_atletas.items():
        a = int(v)
        d = 100
        t = (2*d/a)**(1/2)
        dic[k] = t
    return dic