def calcula_tempo (dic):
    for nome in dic:
        a = (dic[nome])
        t = (200/a)**(1/2)
        dic[nome] = t
    return dic
