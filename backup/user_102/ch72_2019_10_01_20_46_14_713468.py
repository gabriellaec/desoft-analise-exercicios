def lista_caracteres (x):
    i = 0
    d = []
    while i<len(x):
        if x[i] not in d:
            d.append(x[i])
        i+=1
    return d