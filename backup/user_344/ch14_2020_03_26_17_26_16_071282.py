import math
def calcula_distancia_do_projetil(v, t, yo):
    g=9.8
    pt1 = ((v**2)/(2*g))
    pt2 = (1 + (1 + ((2*g*yo)/((v**2)*(math.sin(t))**2))))
    pt3 = math.sin(2*t)
    d = pt1 * pt2 * pt3                 
