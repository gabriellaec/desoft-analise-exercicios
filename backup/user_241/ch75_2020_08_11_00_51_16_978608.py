def verifica_primo(x):
    if x < 2:
        return False
    i = 2
    while i < x:
        if x % i == 0:
            return False
        i += 1
    return True

def verifica_primos(lista):
    dicionario = {}
    for num in lista:
        dicionario[num] = verifica_primo(num)
    return dicionario