def verifica_quadrado_perfeito (n):
    m = n
    par = 0
    while m > 0:   
        m = m - par *2
        par+=2
    if m**2 == n:
        return True
        
    else:
        return False