
def medias_por_inicial(dic):
    d = {}
    for each in dic:
        if each[0] in d:
            d[each[0]] = (d[each[0]]+dic[each])/2
        else:
            d[each[0]] = dic[each]
    return d