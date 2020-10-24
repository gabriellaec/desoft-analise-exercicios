def verifica_quadrado_perfeito (n):
    m=n
    c=0
    while m >= 0:
        if c%2==0:
            m-=c
        c+=1
    if m**2 == n:
        return True
    else:
        return False