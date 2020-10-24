def verifica_primos(x):
    i = 2
    if x < 2:
        return False
    while i < x :
        if x % i == 0:
            return False
        i += 1
    return True