def inverte_lista(lista):
    nova = []
    i = 0
    for a in range(len(lista),-1,-1):
        x = lista[a]
        nova[i].append(x)
        i += 1
    return nova