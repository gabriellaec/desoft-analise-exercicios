def verifica_quadrado_perfeito(n):
    m=0
    m=n
    while m>=0:
        m-=((2 +2*(n-1)+2)*n/2)
        if m**2==n:
            return True
        else:
            return False