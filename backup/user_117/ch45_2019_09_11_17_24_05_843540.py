def zera_negativos(lista):
    z = []
    i = 0
    while i < len(lista):
        if lista[i] < 0:
            z.append(0)
        else:
            z.append(lista[i])
        i+=1
    return z