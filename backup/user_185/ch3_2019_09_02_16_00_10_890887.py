import math
euler = math.exp
pi = math.pi
raiz = math.sqrt
def calcula_gausiana(x , mi , sigma):
    a = 1 / (sigma * raiz (2 * pi))
    b = euler( -0.5 * ((x * mi) / sigma)**2)
    return a * b