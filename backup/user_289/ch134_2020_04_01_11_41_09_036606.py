def verifica_quadrado_perfeito(n):
    M = n
    contador = 1
    while M >= 0:
        contador += 1
        M = M - 2*contador
    if M**2 == n:
        return True
    else:
        return False
        