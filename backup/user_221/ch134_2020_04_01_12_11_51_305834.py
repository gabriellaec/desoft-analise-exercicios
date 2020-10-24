def verifica_quadrado_perfeito(n):
    m = n
    i = 2
    while m > 0:
        if 2 < i:
            m = n - i
        i = i + 2
    if m**2 == n:
        return True
    elif m**2 != n:
        return False