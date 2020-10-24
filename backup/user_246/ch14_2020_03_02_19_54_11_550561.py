import math
def calcula_distancia_do_projetil(x,y,z):
    g=9.8
    d=x**2/9*2(1+(1+(2*g*z)/(x**2(sin(y))**2))**-1)*sin(2*y)
    return d