
def inverte_lista(lista):
    lista2 = []
    i = 1
    while len(lista) - i >= 0:
        lista2.append(lista[len(lista) - i])
        i += 1
    return lista2