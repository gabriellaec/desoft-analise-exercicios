newlist = []
def numero_no_indice(lista):
    for i in range len(lista):
        if lista[i] == i:
            newlist.append(lista[i])
    return newlist