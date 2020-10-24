def verifica_quadrado_perfeito(n):
    m=n
    x=1
    while m>0:
        m-=2*x
        x+=1
    if m**2 == n:
        return True
    else:
        return False