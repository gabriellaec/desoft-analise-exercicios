import math
def calcula_gaussiana (x, u, o):
    p1 = 1/(o**((1/2)*2*math.pi))
    p2 = math.e**(-0.5*((x-u)/o)*2)
    p3 = p1*p2
    return p3