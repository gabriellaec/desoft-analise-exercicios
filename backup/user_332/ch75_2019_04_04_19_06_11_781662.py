def verifica_primos (lista):
    d = {}
    for n in lista:
        if n <= 1:
            d[n] = False
        elif n == 2:
            d[n] = True
        else:
            i = 2
            while i < n:
                if n % i == 0:
                    d[n] = False
                else:
                    d[n] = True
                i += 1
    return d