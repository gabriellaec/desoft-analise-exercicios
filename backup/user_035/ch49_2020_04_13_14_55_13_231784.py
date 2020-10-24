def inverte_lista(lista):
    l = [] 
    for i in range(len(lista)-1):
        l.append(lista[len(lista)-i])
    return l