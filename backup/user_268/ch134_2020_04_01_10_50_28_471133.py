def verifica_quadrado_perfeito(n):
    m = n
    i = 2
    while m >= 0:
        m-=i
        i+=2
    if (m**2) == n:
        return True
    else:
        return False