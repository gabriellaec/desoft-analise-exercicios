def lista_primos(n):
    primos = 2
    while (primos<n):
        primos = primos%2!=0
        return list(primos)