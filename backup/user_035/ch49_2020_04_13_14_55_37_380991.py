def inverte_lista(lista):
    l = [] 
    for i in range(len(lista)):
        l.append(lista[len(lista)-i])
    return l