
def zera_negativos(x):
    n = 0
    y = []
    while n < len(x):
        if x[n] < 0:
            x[n] = 0
            y.append(x[n])
            n = n+1
        else:
            y.append(x[n])
            n = n + 1
    return y

