import math
def calcula_gaussiana(x,mi,sigma):
    A = 1/((sigma*(2*math.pi)^1/2))
    B = math.e^(0.5*((x-mi)/sigma)^2)
    f = A*B
    return f
