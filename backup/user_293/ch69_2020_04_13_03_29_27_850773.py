def junta_listas(lista):
    lista_nova = []
    for e in lista:
        for i in e:
            lista_nova.append(i)
    return lista_nova