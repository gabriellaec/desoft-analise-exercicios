def verifica_primos(numeros):
    primo = {}
    for n in numeros:
        x = 2
        for x < n:
            if n%x==0:
                primos[n] = False
            n+=1
            else:
                primos[n] = True
    return primo 