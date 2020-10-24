import math

def calcula_distancia_do_projetil(v,teta,y0):
    g = 9.8
    rad = math.radians(teta)
    a = (v**2)/(2*g)
    o = 1 + (1 +(2*g*y0)/v**2*(math.sin(rad)**2))**1/2
    dist = a * o * math.sin(2*teta)
    return dist