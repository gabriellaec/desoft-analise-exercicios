import math

def distancia_do_projetil(v, ang, y):
    rad=(ang*math.pi)/180
    g=10
    d=((v**2)/(2*g))*(1+math.sqrt((1+((2*g*y)/(v**2))*(math.sin(rad))**2))*(math.sin(rad*2))
    return d
