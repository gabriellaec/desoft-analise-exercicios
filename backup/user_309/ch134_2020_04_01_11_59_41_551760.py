def verifica_quadrado_perfeito(n):
    m = n
    x = 0 
    while m > 0:
        m = m - (x*2)
        x = x + 1
    if m**2 != n:
        return False
    else:
        return True