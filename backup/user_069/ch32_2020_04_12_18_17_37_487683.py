def eh_primo (n):
    div = 3
    if n%2 == 0 and n != 2 or n == 1 or n == 0:
        return False
    
    while n > div:
        if n%div == 0:
            return False
        div += 1
    return True

def lista_primos (n):
    lista_primos = [0]*n
    i = 0
    e = 0
    while i < n:
        if eh_primo(e) == True:
            lista_primos[i] = e
            e += 1
            i += 1
        else:
            e += 1
    return lista_primos