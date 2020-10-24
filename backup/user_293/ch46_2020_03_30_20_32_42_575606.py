def numero_no_indice(lista):
    lista_f = []
    i = 0
    while i < len(lista):
        if lista[i] == i:
            lista_f.append(lista[i])
        i += 1
    return lista_f