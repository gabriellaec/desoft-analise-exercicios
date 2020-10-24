def eh_primo(n):
    if n == 0 or n == 1:
        return False
    elif n%2==0 and n!=2:
        return False
    else:
        i = 3
        while i < n:
            if n%i==0:
                return False
            i += 2
        return True
def verifica_primos(numeros):
    saoPrimos = {}
    for n in numeros:
        r = eh_primo(n)
        saoPrimos[n] = r
    return saoPrimos