def numero_no_indice(lista):
    i = 0
    new_list = []
    for i in range(len(lista)):
        if lista[i] == i:
            new_list.append(i)
    return new_list