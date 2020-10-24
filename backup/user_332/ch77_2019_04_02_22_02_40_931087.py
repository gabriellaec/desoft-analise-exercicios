def calcula_tempo (dic):
    for nome in dic:
        v = float(dic[nome])
        t = (100/v)
        dic[nome] = t
    return dic


            