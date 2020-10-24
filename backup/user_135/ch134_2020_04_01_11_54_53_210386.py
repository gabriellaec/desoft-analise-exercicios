def verifica_quadrado_perfeito(n):
    m = n
    i = 0
    x = m - i
    while x >= 0:
        x = m - i
        i = i + 2
    y = x * (-1)
    m = y**2
    if m == n:
        return True
    else:
        return False