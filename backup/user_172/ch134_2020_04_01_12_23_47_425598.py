import math
def verifica_quadrado_perfeito (n):
    m=n
    x=2
    while m>-(math.sqrt(n)):
        m=m-x
        x=x+2
    if m**2==n:
        return True
    elif m**2 != n:
        return False
