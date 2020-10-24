def verifica_quadrado_perfeito(n):
    m=n
    s=2
    while m>=0:
        m=m-s
        s=s+2
    if m**2 == n:
        return True
    elif m**2 != n:
        return False