def verifica_primos (lista):
    d = {}
    for n in lista:
        if n <= 1:
            d[n] = False
        for e in range(2,n):
            if n % e == 0:
                d[n] = False
                break
            else:
                d[n] = True
    return d
