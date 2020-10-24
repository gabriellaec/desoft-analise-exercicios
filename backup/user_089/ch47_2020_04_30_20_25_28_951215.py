def estritamente_crescente(x):
    y = []
    for e in x:
        if e not in y:
            y.append(e)
    return y