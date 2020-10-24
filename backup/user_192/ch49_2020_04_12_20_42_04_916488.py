def inverte_lista(x):
    invert = list()
    for i in range(len(x)):
        x.reverse()
        invert.append(x)
    return invert