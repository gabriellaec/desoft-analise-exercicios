import math
def calcula_elongacao(A, phiO, omega, T):
    x=A*math.cos(math.radians(phiO+omega*T))
    return x