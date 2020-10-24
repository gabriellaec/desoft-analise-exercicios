def numero_no_indice(lista):
    lista_nova = []
    for i in range(len(lista)):
        if i == lista[i]:
            lista_nova.append(i)
        i += 1
    return lista_nova