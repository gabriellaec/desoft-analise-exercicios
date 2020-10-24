def verifica_quadrado_perfeito(n):
    m = n 
    a = 0
    while m>0: 
        m -= a*2
        a += 1
    if (m**2) == n:
        return True
    else:
        return False