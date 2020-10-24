def calcula_tempo (dic):
    for nome,v in dic.items():
        t = (100/float(v))
        dic[nome] = t
    return dic

            