from math import sin
g = 9.8
def calcula_distancia_do_projetil(v, o, y):
    d = ((v**2)/(2*g))*(1+(1+((2*g*y)/((v**2)*(sin(o))**2)))**(1/2))*sin(2*o)