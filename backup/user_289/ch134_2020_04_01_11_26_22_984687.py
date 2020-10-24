import numpy as np 
def verifica_quadrado_perfeito(n):
    M = n
    while M >= 0:
        sequência_pares = np.arange(2, M, 2)
        M = M - sequência_pares
    if M**2 = n:
        return True
    else:
        return False
        