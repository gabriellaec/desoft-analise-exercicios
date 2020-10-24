def verifica_quadrado_perfeito(n):
    m = n
    cont = 1
    
    while m > 0:
        m -= 2*cont
        cont += 1
    
    if m**2 == n:
        return True
    
    return False