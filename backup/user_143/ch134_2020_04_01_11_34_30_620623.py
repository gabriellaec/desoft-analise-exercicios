def verifica_quadrado_perfeito(n):
    m=n
    p=0
    while m>=0:
        m-=(2 +2*p)
        p+=1
    d=(m)**2
    if d==n:
        return True
    else:
        return False