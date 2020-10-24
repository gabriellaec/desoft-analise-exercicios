def junta_listas(listas):
    numeros = []
    for i in range(len(listas)):
        for x in range(len(listas[i])):
            numeros.append(listas[i[x]])
    return numeros