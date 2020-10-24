def numero_no_indice(lista):
    index = 0
    while index < len(lista):
        if lista[index] == index:
            Lista.append(lista[index])
            index = index + 1
        else:
            break
    return(Lista)