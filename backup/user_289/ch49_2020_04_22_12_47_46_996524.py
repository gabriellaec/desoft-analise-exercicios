def inverte_lista(lista):
    lista_invertida = []
    i = len(lista)
    while i <= len(lista):
        lista_invertida.append(lista[i])
        i -= 1
    return lista_invertida