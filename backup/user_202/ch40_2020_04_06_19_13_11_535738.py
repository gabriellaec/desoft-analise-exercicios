def soma_valores(x):
    a = 0
    t = 0
    for i in x:
        a = x[i-8]
        t += a
    return t