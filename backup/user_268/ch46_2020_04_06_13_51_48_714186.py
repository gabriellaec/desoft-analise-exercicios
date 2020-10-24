def numero_no_indice(list):
    a = len(list)
    lista = []
    for i in range(a):
        if list[i] == i :
            lista.append(i)
    return lista
            