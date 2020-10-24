def verifica_primos(numeros):
    primos={}
    for e in numeros:
        if e<=1:
            primos[e]=False
        elif e==2:
            primos[e]=True
        i=2
        while i<e:
            if e%i==0:
                primos[e]=False
            i+=1
        i=2
        while i<e:
            if e%i!=0:
                primos[e]=True 
            
    return primos 