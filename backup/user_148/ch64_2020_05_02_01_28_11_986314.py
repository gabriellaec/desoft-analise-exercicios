def acha_bigramas(str):
    lista = []
    i = 0
    while i<len(str)-1:
        lista.append(str[i:i+2])
        i += 1
    k = 0
    while k<len(lista):
        if lista.count(lista[k])>1:
            del lista[k]
        k += 1
    return lista