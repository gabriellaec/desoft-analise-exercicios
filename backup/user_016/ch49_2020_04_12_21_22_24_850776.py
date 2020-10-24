lista2 = []
def inverte_lista(lista):
    i = 1
    while len(lista) - i >= 0:
        lista2.append(lista[len(lista) - i])
    return lista