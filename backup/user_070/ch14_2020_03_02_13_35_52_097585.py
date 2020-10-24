import math
g=9.8
def calcula_distancia_do_projetil(v,a,h):
    d=((v**2)/(2*g))*(1+(1+(2*g*h)/v**2*(math.sin(a))**2)**(1/2))*(math.sin(2*a))
    return d