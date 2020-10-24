def junta_listas(lista):
    contador = True
    i = 0
    lista_nova = []
    while i < len(lista):
        x = lista[i]
        lista_nova += x
        i += 1
    return lista_nova