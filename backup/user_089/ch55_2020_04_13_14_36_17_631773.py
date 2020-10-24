def encontra_maximo(x):
    y = []
    for e in x:
        for i in e:
            y.append(i)
    return max(y)