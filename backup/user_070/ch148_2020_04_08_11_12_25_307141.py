def conta_letras(x):
    dicio = {}
    for i in x:
        if i not in dicio:
            dicio[i] = 1
        else:
            dicio[i] += 1
    return dicio