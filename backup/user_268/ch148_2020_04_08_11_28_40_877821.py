def conta_letras(lista):
    dicio = {}
    for i in lista:
        if not i in dicio:
            dicio[i] = 1
        else:
            dicio[i] += 1
    return dicio