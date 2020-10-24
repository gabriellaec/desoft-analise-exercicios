def inverte_lista (lista):
    l2 = []
    m = 1
    tam = len(lista)
    for i in range (0,tam):
        l2.append(lista[tam-m])
        m+=1
    return l2