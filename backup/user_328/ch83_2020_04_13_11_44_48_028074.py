def medias_por_inicial(lista):
    dict= {}
    lista2= []
    for k,v in lista.items():
        y = v
        x = k
        if x[0] not in dict:
            dict[x[0]] = y
        elif x[0] in dict:
            dict[x[0]] = (dict[x[0]] + y)/2
    return dict