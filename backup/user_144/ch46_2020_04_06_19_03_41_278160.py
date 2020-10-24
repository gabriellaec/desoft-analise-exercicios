def numero_no_indice(lista):
    i = 0
    new_list = []
    while i < len(lista):
        if lista[i] == i:
            new_list.append(i)
            i +=1
    return new_list