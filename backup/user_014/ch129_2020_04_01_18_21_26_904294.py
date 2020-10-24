def verifica_quadrado_perfeito(n):
    numero_impar = 1
    while n > numero_impar:
        n = n - (2 * numero_impar + 1)
        numero_impar += 1
    if numero_impar == 0:
        return True
    else:
        return False