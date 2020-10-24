def acha_bigramas(string):
    lista = []
    list2 = []
    for k in range (0, len(string)):
        if len(string[k:k+2])>1:
            lista.append(string[k:k+2])
    for e in lista:
        if e not in list2:
            list2.append(e)
    return list2
