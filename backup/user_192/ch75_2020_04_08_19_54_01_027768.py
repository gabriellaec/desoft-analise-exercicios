def verifica_primos(numeros):
    primo = {}
    for n in numeros:
        if n%n==0 n%1==0:
            primo[n] = True
        else:
            primo[n] = False
        
    return primo 