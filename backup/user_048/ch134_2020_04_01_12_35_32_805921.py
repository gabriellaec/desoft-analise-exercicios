import math
def verifica_quadrado_perfeito(n):
    m=n
    while m>=0:
        p=2
        m=m-p
        p=p+2
    if (m**2)==n:
        return True
    else:
        return False
    