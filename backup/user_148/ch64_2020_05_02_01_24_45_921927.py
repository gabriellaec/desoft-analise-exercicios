def acha_bigramas(str):
    lista = []
    i = 0
    while i<len(str):
        lista.append(str[i:i+2])
        i += 1
    k = 0
    while k<len(lista):
        if lista[i].count()>1:
            del lista[i]
        k += 1
    return lista