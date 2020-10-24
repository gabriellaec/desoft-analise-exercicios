def inverte_lista(lista):
    lista_nova = []
    i = 0
    n = 1
    while i < len(lista):
        lista_nova.append(lista[len(lista)-n])
        n += 1
        i += 1
    return lista_nova