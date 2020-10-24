def verifica_quadrado_perfeito:
    m = n
    i = 0
    while m >= 0:
        m = m - (i*2)
        i = i + 1
    if m**2 == n:
        return True
    else:
        return False