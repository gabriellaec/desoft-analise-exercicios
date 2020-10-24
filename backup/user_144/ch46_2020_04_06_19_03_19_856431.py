def numero_no_indice(lista):
    i = 0
    new_list = []
    while i < len(lista):
        if lista[i] == i:
            i +=1
            new_list.append(i)
    return new_list