def numero_no_indice(lista):
    listanova = []
    for e in range(0, len(lista)):
        if lista[e]==e:
            listanova.append(e)
    return listanova