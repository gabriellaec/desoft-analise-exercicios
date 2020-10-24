def verifica_quadrado_perfeito(n):
    m = n
    j = 2
    while m > 0:
        m -= j
        j += 2
    if m*m == n:
        return True
    else:
        return False
