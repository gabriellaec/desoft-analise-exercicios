def inverte_lista(lista):
    i = len(lista) - 1
    o = []
    while i < len(lista):
        o.insert(lista[i])
        i +=1
    return o