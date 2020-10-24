def verifica_primos(x):
    i = 2
    while i < x:
        if x % i == 0:
            return False
        i += 1
    return True
def maior_primo_menor_que(n):
    i = n
    if n < 2:
        return -1
    while i >= 2:
        if verifica_primos(i):
            return n
        i -= 1
    return -1