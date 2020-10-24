def verifica_quadrado_perfeito(n):
    m = n

    subtrair = 2
    while m >= 0:
        m-=subtrair
        subtrair+=2
    
    if m**2 == n:
        return True
    else:
        return False