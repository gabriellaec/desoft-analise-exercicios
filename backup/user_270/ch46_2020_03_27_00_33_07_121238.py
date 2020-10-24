def numero_no_indice(list):
    i = 0
    lista = []
    while i < len(list):
        if list[i] == i:
            lista.append(i)
    i += 1
    return lista