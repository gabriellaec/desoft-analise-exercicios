def numero_no_indice(lista):
    listax = []
    i = 0
    while i < len(lista):
        if lista[i] == i:
            listax.append(i)
        i += 1
    return listax