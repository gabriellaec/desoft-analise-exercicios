def verifica_quadrado_perfeito(n):
    m=n
    while m<0:
        m=n-2
    if m**2==n:
        return True
    else:
        return False