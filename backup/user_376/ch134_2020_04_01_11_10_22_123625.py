def verifica_quadrado_perfeito(n):
    m=n
    k=2
    while m>=0:
        m=m-k
        k=k+2
    if m**2 == n:
        return True
    else:
        return True