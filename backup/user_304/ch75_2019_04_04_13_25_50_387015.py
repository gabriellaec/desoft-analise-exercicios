def verifica_primos(numeros):
    primos={}
    for e in numeros:
        if e<=1:
            primos[e]=False
        elif e%2==0 and 2!=2:
            primos[e]=False
        i=2
        while i<e:
            if e%i==0:
                primos[e]=False
            else:
                primos[e]=True
            i+=1
    return primos 