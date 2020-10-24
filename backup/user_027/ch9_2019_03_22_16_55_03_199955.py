def lista_sufixos(x):
    i = 0
    tam = len(x)
    y = []
    while i < tam:
        y.append(x[i])
        i += 1
    return y