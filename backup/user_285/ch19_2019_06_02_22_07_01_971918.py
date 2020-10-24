import math
g=9.8
def calcula_distancia_do_projetil(v,teta,y):
    a=v**2/2*g
    b=math.sin(2*teta)
    c= 1 + ((2*g*y)/v**2*(math.sin(teta))**2)
    distancia=a*b*(1 + c**0.5)
    return distancia
                                                       