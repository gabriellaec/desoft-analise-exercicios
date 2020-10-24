def soma_impares(lista):
    i = 0
    s = 1
    while i < len(lista):
        if (-1)**(lista[i]) == -1:
            s += lista[i]
            i += 1
    return s