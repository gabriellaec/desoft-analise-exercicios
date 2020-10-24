def estritamente_crescente(lista):
    lista_nova = []
    for i in range(len(lista)):
        if (i + 1) > i in lista:
            lista_nova.append(i)
    return lista_nova
            