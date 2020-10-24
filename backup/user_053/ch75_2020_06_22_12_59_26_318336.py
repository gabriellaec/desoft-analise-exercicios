from math import sqrt

def verifica_primo(numero):
    if numero <= 1:
        return False
    elif numero == 2: 
        return True
    else:
        i = 3
        while i < numero:
            if numero %i == 0 or numero %2 == 0:
                return False
            i += 2
        return True


def verifica_primos(lista_numeros):
    respostas = {}
    for n in lista_numeros:
        respostas[n] = verifica_primo(n)
    return respostas