def numero_no_indice(lista):
    iguais = []
    size = len(lista)
    i = 0
    while i<size:
        if lista[i] == i:
            iguais.append(i)
        i += 1
    return iguais