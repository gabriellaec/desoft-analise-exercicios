def inverte_lista(lista):
    nova = []
    for a in range(len(lista),-1,-1):
        x = lista[a]
        nova.append(x)
    return nova