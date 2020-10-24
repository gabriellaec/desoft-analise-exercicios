def conta_bigramas(str):
    lista = []
    dic = {}
    i = 0
    while i<len(str):
        lista.append(str[i:i+2])
        x = lista.count(lista[i])
        dic[lista[i]] = x
        i += 1
    return dic
        