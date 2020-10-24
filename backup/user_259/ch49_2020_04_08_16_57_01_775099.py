def inverte_lista(lista):
    lista_invertida = lista[len(lista)-1]
    i = 1
    while i<len(lista):
        lista_invertida[i] = lista((len(lista))-(1+i))
    return lista_invertida