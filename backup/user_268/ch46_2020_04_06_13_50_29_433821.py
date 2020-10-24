def numero_no_indice(list):
    a = len(list)
    lista = []
    for i in range(list):
        if list[i] == i :
            lista.append(i)
    return lista
            