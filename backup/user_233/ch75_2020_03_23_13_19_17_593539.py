def eh_primo(n):
    
    if n <= 0 or n == 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    
    divisor = 3
    while True:
        if divisor == n: return True
        if n % divisor == 0: return False
        divisor += 2

def verifica_primos(numeros):
    
    primos = {}
    
    for n in numeros:
        primos[n] = eh_primo(n)
    
    return primos
        