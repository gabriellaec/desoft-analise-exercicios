def numero_no_indice(lista):
    lista_indices = []
    for i in range(len(lista)):
        if i == lista[i]:
            lista_indices.append(lista[i])
    return lista_indices

