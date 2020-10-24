def calcula_tempo (dic):
    for nome in dic:
        v = dic[nome]
        t = (100/v)
        dic[nome] = t
    return dic


            