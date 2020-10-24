def isPrimo(n):
    test = 2
    while(test < n):
        if ((n % test) == 0):
            return False
        test = test + 1
    return True

def verifica_primos(lista):
    result = {}
    
    for x in lista:
        result[x] = isPrimo(x)
    return result