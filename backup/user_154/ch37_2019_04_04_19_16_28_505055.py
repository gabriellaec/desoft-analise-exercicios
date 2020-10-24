import math

def eh_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    
    for test in range(3, math.floor(mat.sqrt(n)) + 1, 2):
        if n % test == 0:
            return False
    return True

def imprime_primos(n):
    for x in range(2, n):
        if eh_primo(x):
            print(x)
    return