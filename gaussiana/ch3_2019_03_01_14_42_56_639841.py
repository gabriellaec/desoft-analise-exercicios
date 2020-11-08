import math
def calcula_gaussiana(x,u,a):
    if a > 0:
        f = (1/(a*math.sqrt(2*math.pi)))**(-0.5(((x-u)/a)**2))
        return f