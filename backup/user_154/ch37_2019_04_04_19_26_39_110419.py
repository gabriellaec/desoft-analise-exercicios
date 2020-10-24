def eh_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    
    for test in range(3, n, 2):
        if n % test == 0:
            return False
    return True

def imprime_primos(n):
    contador = 0
    x = 0
    
    while contador != n:
        if eh_primo(x):
            print(x)
            contador = contador + 1
        x = x + 1
    return