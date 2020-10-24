def isPrimo(n):
    test = 2
    while(test < n):
        if ((n % test) == 0):
            return False
        test = test + 1
    return True

def imprime_primos(n):
    if (n < 2):
        return -1
    while n > 1:
        if isPrimo(n):
            print(n)
        n = n - 1
    return