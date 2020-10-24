def numero_no_indice(lista):
    x = len(lista)
    i = 0
    a = []
    while i < x:
        if lista[i] == i:
            a.append(i)
            i += 1
        else:
            i += 1
    return a