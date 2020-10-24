import math
def  calcula_distancia_do_projetil(v, o, y):
    g= 9.8
    k= math.sin(o)
    w= v**2/(2*g)
    q= 1 + (1 + (2*g*y/((v**2)*(k)**2)))**(1/2)
    a= math.sin(2*o)
    d= w*q*a
    return d