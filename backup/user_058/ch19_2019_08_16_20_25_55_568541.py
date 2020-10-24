from math import sin
from math import sqrt
def calcula_distancia_do_projetil(v,g,y,a):
    d= (v**2)/(2*g)*(1+sqrt(1+(2*g*y/(v**2)*((sin(a))**2))))*sin(2*a)
    return d