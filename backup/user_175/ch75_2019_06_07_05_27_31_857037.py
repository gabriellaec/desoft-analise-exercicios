from math import sqrt
def testa_primo(x):
    x = int(x)
    cont = 2
    if x == 2:
        return True
    elif x < 2:
        return False
    while cont <= sqrt(x):
        if x % cont == 0:
            return False
        else:
            cont += 1
    return True

def verifica_primos(x):
    dicionario = {}
    for i in x:
        dicionario[i] = testa_primo(i)
    return dicionario