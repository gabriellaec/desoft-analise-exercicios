def numero_no_indice(lista):
    num_ind = []
    i = 0
    while i<len(lista):
        if lista[i] == i:
            num_ind.append(i)
        i+=1
    return num_ind