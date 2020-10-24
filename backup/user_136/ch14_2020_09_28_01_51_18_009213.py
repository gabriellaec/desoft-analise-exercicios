import math
def  calcula_distancia_do_projetil(v, y, o):
    g= 9.8
    w= (v**2)/2*g
    q= (1+(1+(2*g*y)/(v**2)*(math.sin(o))**2)*math.sin(2*o))
    a= w*q
    return a