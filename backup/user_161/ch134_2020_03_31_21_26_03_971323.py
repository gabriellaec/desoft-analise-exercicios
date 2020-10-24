def verifica_quadrado_perfeito(n):
    m = n
    pares = 2
    contador = 0
    while m >= 0:
        m -= pares
        pares += 2
    if m**2 == n:
        return True
    else:
        return False