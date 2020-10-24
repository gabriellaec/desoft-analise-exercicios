def medias_por_inicial(lista):
    dic = {x:lista.count(x) for x in lista }
    return max(dic, key=dic.get)