def inverte_lista(lista):
    lista_invertida = []
    while len(lista) > 0:
        lista_invertida.append(lista[-1])
        del lista[-1]
    return lista_invertida