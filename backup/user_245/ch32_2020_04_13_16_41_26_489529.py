def lista_primos(n):
    primos = []
    
    if n ==1:
        return False
    for d in range(2,n):
        if n%d ==0:
            return False
        else:
            primos.append(d)
    return primos