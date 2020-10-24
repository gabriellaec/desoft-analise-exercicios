def verifica_primo(x):
    i = 2
    while i < x:
        if x % i == 0:
            return False
        i += 1
    return True
def verifica_primos(lista):
    dicionario = {}
    for num in lista:
        dicionario[str(num)] = verifica_primo(num)
    return dicionario