def eh_primo (n):
    i = 3
    if n == 2:
        return True
    elif n == 0 or n == 1 or n%2 == 0:
        return False
    elif n < 0:
        return False
    else:
        while i < n:
            if n%i == 0:
                return False
            i = i + 2
        return True
    
def verifica_primos (lista):
    i = 0
    dicionario = {}
    while i < len(lista):
        dicionario[lista[i]] = eh_primo(lista[i])
        i = i + 1
    return dicionario