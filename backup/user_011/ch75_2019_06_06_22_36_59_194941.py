def verifica_primos(numeros):
    dicio = {}
    i = 0
    while i< len(numeros):
        n = numeros[i]
        if n % 2 and n % 3 and n % 5 and n % 7 != int:
            dicio[n] = 'é primo'
        else:
            dicio[n] = 'n é primo'
        i += 1
    return dicio