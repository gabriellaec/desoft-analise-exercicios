def numero_no_indice (lista):
    lista2 = []
    i = 0
    while i < len(lista):
        if i == lista[i]:
            lista2.append(i)
            i += 1
        else:
            i += 1
    return lista2