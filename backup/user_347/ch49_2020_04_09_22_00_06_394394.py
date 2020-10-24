def inverte_lista(lista):
    i = len(lista) - 1
    o = []
    while i < len(lista):
        o.insert(0, lista[i])
        i +=1
    return o