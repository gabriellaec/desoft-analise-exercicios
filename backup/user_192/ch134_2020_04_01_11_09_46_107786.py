def verifica_quadrado_perfeito(n):
    m = n
    while m > 0:
        par = par + 2
        m = m - par
        if m**2 == n:
            return True
        else:
            return False
    