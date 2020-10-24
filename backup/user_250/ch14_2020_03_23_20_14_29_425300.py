import math

def calcula_distancia_do_projetil(v, teta, y):
    g=9.8
    a=(v**2)/(2*g)
    b=(v**2)*(math.sin(teta))**2
    c=2*g*y
    d=(1+c/b)**(1/2)
    e=(1+d)*(math.sin(2*teta))
    distancia=a*e
    return distancia