def inverte_lista(lista):
    if not lista:
        return lista
    return lista[-1:] + inverte_lista(lista[:-1])