def junta_listas(lista):
    lista_nova = []
    for i in range(len(lista)):
        lista_nova.append(lista.pop(i))
    return lista_nova