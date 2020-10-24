def lista_primos(n):
    primos = [0]*n
    i = 2
    primos[0] = 2
    if n > 0:
        primos[1] = 3
        while i < n:
            primos[i] = primos[i-1] + 2
            i += 1
    return primos