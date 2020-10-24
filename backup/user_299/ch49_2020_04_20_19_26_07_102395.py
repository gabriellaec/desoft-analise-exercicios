def inverte_lista(lista):
    listainvertida = [0]*len(lista)
    i=0
    while i<len(lista):
        listainvertida[-i] = lista[i]
    listainvertida.append(listainvertida[0])
    del listainvertida[0]
    return listainvertida