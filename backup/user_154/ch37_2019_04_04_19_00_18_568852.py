def eh_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    test = 2
    while(test < n):
        if ((n % test) == 0):
            return False
        test = test + 1
    return True

def imprime_primos(n):
    for x in range(2, n):
        if eh_primo(x):
            print(x)
    return