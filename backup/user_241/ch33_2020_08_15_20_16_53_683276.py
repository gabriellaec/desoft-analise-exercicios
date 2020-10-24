def verifica_primos(x):
    i = 2
    if x < 2:
        return False
    while i < x :
        if x % i == 0:
            return False
        i += 1
    return True

def primos_entre(a,b):
    i = 0
    for num in range(a,b+1):
        if verifica_primos(num):
            i += 1
    return i