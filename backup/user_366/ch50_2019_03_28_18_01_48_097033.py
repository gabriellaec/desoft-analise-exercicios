def numero_no_indice(lista):
    new = []
    i = 0
    while i < len(lista):
        if i == lista[i]:
            new.append(lista[i])
        i += 1
    return new