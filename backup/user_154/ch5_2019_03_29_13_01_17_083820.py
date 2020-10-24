def isPrimo(n):
    test = 2
    while(test < n):
        if ((n % test) == 0):
            return False
        test = test + 1
    return True

def maior_primo_menor_que(n):
    if (n < 2):
        return -1
    while(isPrimo(n) == False):
        n = n - 1
    return n