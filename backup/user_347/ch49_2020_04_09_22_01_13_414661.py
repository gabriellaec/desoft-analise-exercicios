def inverte_lista(lista):
    i = len(lista) - 1
    o = []
    while i < len(lista):
        o.extend(lista[i])
        i +=1
    return o