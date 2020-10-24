def conta_letras(x):
    d = {}
    l = list(x)
    for i in range(len(l)):
        if l[i] not in d:
            d[l[i]] = 1
        else:
            d[l[i]] += 1
    return d