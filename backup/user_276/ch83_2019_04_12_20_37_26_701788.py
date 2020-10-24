dic = {}
def medias_por_inicial(dic):
    for k,v in dic.values:
        dic[k[0]] = v
    return dic