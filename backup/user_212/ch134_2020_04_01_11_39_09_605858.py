def verifica_quadrado_perfeito(n):
    m= n
    i= 0
    while (m >=0):
        m -= i*2
        i += 1 
    if m**2 == n**2:
        return True 
    elif m**2 != n**2:
        return False 
     