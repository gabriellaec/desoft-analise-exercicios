def eh_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i < n:
        if n % i == 0:
            return False
        i += 2
    return True

def verifica_primos(lista):
    dicionario = {}
    for i in lista:
        dicionario[lista[i]] = eh_primo(lista[i])
    return dicionario