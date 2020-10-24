def verifica_primos(x):
    r = {}
    for i in range(2, x):
        if x % i != 0:
            r[x] = True
    return r