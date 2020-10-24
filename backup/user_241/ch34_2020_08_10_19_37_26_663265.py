def verifica_primos(x):
    i = 2
    while i < x:
        if x % i == 0:
            return False
        i += 1
    return True
def maior_primo_menor_que(n):
    if verifica_primos:    
        return n
    elif n > 0:
        return verifica_primos(n)
    elif n < 0:
        return -1
