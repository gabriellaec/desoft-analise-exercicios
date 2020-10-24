import numpy as np

def eh_primo(numero):
    divisor = 2
    i = 0
    lista = np.arrange(3, numero, 2)
    if lista[-1] != numero:
        lista.append(numero)
    while divisor <= numero:
        if numero%divisor == 0:
            return False
            break
        else:
            divisor = lista[i]
            i += 1