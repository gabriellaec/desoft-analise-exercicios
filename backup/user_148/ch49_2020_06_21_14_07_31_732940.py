def inverte_lista(lista):
    l2 = []
    i = 1
    while i <= len(lista):
        l2.append(lista[len(lista) - i])
        i += 1
        
    return l2