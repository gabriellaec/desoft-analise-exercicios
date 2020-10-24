def verifica_quadrado_perfeito(n):
    m = n
    c = 2 
    while m > 0:
        m = m - c
        c += 2
    if (m**2) != n:
        return False
    else:
        return True