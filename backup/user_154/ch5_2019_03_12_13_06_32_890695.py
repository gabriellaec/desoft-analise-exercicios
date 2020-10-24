def maior_primo_menor_que(n):
    if (n < 1):
        return -1
    while(!isPrimo(n)):
        n++
    return n

def isPrimo(n):
    test = 2
    while(test < n):
        if ((n % test) == 0):
            return False
        test = teste + 1
    return True