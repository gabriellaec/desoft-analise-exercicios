def verifica_quadrado_perfeito(n):
    i=-2
    m=n+i
    while m>=0:
        m+=i
        i-=2
    if m**2==n:
        return True
    else:
        return False
    

    
    