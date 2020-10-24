def verifica_quadrado_perfeito(n):
    m=n
    d=d+2
    while m>0:
        m=m-d
        if m**2==n:
            n = True
        else:
            n = False
        