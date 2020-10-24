def numero_no_indice(lista):
    lista_nova = []
    i = 0
    for e in lista:
        if e == i:
            lista_nova.append(e)
        i += 1
    return lista_nova