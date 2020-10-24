def encontra_maximo(x):
    y = []
    for e in x:
        for i in e:
            y.append(abs(i))
    return max(y)