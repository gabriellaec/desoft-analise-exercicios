import math
def calcula_gaussiana (x, u, o):
    p1 = 1/(o*((2*math.pi)**(1.2)))
    p2 = math.exp(-0.5*((x-u)/o)**2)
    p3 = p1*p2
    return p3