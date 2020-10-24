def verifica_quadrado_perfeito(n):
    m=n
    i=2
    while m > -1:
        m=m-i
        i=i+2
        
    if m**2 == n:
        return True
    else:
        return False