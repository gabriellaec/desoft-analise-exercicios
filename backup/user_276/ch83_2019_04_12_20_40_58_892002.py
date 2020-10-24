dicnovo = {}


def medias_por_inicial(dic):
    for k, v in dic.values:
        dicnovo[k[0]] = v
    return dicnovo
