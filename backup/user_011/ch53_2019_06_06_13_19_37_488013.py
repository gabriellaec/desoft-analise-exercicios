def inverte_lista(lista):
    lista_invertida = []
    i = len(lista)
    while i > 0:
        a = lista[i - 1]
        lista_invertida.append(a)
        i-=1
    return lista_invertida
    