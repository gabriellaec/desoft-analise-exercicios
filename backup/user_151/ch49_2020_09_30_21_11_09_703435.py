def inverte_lista(x):
    i = len(x)

    y = []
    while i > 0:
        y.append(x[i-1])
        i = i - 1
    return y
        