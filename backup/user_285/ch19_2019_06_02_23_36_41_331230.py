import math
g=9.8
def calcula_distancia_do_projetil(v,teta,y):
    a=v**2/2*g
    b=math.sin(2*teta)
    c= 1 + ((2*g*y)/(v * (math.sin(math.radians(teta))))**2)
    distancia=a*(1 + c**0.5)*b
    return distancia
                                                       