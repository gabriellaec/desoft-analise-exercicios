def verifica_quadrado_perfeito(n):
    m=n
    x=2
    while m>=0:
        m=m-x
        x+=2
    if m<0 and m**2==n:
        return True
    elif m<0 and m**2!=n:
        return False