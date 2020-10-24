def eh_primo(num):
    if num == 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    i = 2
    while i < num/2:
        impar = 2*i - 1
        if num % impar == 0:
            return False
        i += 1
    return True

def lista_primos(n):
    i = 0
    primos = []
    while len(primos) < n:
        if eh_primo(i):
            primos.append(i)
        i += 1
    return primos

