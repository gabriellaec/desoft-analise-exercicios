def verifica_quadrado_perfeito(n):
    m=0
    m=n
    while m>=0:
        m=m-((2 +2*(n-1)+2)*n/2)
    d=m**2
    if d==n:
        return True
    else:
        return False