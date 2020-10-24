def inverte_lista(lista):
    lista_invertida = []
    i = 0
    while i<len(lista):
        lista_invertida[i] = lista((len(lista))-(1+i))
    return lista_invertida