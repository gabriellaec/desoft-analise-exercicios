def inverte_lista(lista):
    var = 0
    lista_inv = []
    while var != len(lista):
        lista_inv.append(lista[-1])
        lista.remove(lista[-1])

    return lista_inv