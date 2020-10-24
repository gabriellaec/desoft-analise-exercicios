def verifica_quadrado_perfeito(n):
    m = n
    x = 2
    while(m>=0):
        m = m - x
        x = x +2
    m = m*m
    if(m==n):
        return True
    else:
        return False
        