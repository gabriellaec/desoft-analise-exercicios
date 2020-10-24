def inverte_lista(lista):
    listainvertida = [0]*len(lista)
    for i,e in enumerate(lista):
        listainvertida[-i] = e
    listainvertida.append(listainvertida[0])
    del listainvertida[0]
    return listainvertida