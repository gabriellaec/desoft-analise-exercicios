def verifica_quadrado_perfeito(n):
    if n == 1:
        return True
    m = n
    i = 2
    while m >= 0:
        m -= i
        i += 2
    if m == n:
        return True
    else:
        return False