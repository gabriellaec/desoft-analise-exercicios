def verifica_primos(x):
    i = 2
    while i < x:
        if x % i == 0:
            return False
        i += 1
    return True
def maior_primo_menor_que(n):
    if verifica_primos(n):    
        return n
    elif n > 0:
        return verifica_primos
    elif n < 0:
        return -1
