def inverte_lista(lista):
    newlist = []
    for i in range (len(lista)-1, -1, -1):
        newlist.append(lista[i])
        return newlist