def verifica_quadrado_perfeito(n):
    m=n
    k=0
    while m>-1:
        m=m-k
        k=k+2
    if m**2 == n:
        return True
    elif m**2 != n:
        return True