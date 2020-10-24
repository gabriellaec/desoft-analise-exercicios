def inverte_lista(x):
    i = 0
    y = []
    while i < len(x):
        y.append(x[len(x) - 1 - i])
        i += 1
    return y