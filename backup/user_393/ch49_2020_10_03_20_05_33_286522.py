def inverte_lista(lista):
    lista_invertida= []
    i= 1
    while i <= len(lista):
        lista_invertida.append(lista[-i])
        i= i + 1
    return lista_invertida