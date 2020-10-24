def inverte_lista(lista):
    nova = []
    #i = 0
    for a in range(len(lista)-1,-1,-1):
        nova.append(lista[a])
        #i += 1
    return nova