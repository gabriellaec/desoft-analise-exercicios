def zera_negativos(lista):
    i = 0
    a = 0
    nova = []
    while a < len(lista):
        if lista[i] < 0:
            nova.append(0)
            i += 1
            a += 1
        else: 
            nova.append(lista[i])
            i += 1
            a += 1

    return nova