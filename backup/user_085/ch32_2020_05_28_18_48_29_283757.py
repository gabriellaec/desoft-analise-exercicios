def lista_primos(n):
    numeroPb = list(range(3, n))
    numeroPa = list(range(3, n))
    for x in numeroPb:
        for i in range(2, x):
            if x % i == 0:
                numeroPa.remove(x)
                break
    return numeroPa