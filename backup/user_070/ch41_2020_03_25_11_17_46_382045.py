def zera_negativos(lista):
    a = len(lista)
    i = 1
    while i<=a:
        n = lista[i-1]
        if n<0:
            lista[i-1] = 0
            i += 1
        else:
            i += 1
    return lista