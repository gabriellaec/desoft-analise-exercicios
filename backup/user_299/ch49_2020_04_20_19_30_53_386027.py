def inverte_lista(lista):
    listainvertida = [0]*len(lista)
    i=0
    while i<len(lista):
        listainvertida[-i] = lista[i]
        i = i+1
    if listainvertida[0] == lista[0]:
        listainvertida.append(listainvertida[0])
        del listainvertida[0]
    return listainvertida