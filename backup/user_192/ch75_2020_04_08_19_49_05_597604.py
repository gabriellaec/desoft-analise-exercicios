def verifica_primos(numeros):
    primo = {}
    for n in numeros:
        x = 2
        for x < n:
            if x%n==0:
                primos[n] = False
            else:
                primos[n] = True
    return primo 