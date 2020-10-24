def junta_listas(listas):
    numeros = []
    for i in range(len(listas)):
        a = listas[i]
        for x in range(len(listas[i])):
            numeros.append(a[x])
    return numeros