def verifica_quadrado_perfeito(n):
    m=n
    i=0
    while m >= 0:
        i+=1
        m = m- 2*contador
    if m**2 == n:
        return True
    else:
        return False