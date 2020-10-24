def mais_frequente(lista):
    dicio = {}
    for a in lista:
        if a in dicio:
            dicio[a] += 1
        else:
            dicio[a]=1
    for m in dicio:
        m = dicio[i]
        if dicio[i] > dicio[a]:
            return m
    