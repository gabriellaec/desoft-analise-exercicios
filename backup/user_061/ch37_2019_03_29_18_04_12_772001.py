def eh_primo(p):
    if p < 2:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    i = 3
    while i < p:
        if p % i == 0:
            return False
        i += 2
    return True
def imprime_primos(n):
    f=0
    while f<n:
        if eh_primo(f) == True:
            print(f)
        f+=1
