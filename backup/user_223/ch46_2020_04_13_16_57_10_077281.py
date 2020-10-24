def numero_no_indice(lista):
    newlist = []
    for i in range (len(lista)):
        if lista[i] == i:
            newlist.append(lista[i])
    return newlist