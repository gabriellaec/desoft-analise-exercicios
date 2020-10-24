def inverte_lista(lista):
    i = 0
    lista_invertida = [0]*len(lista)
    while i<len(lista):
        lista_invertida[i] = lista[len(lista)-i-1]
        i+=1
    return lista_invertida