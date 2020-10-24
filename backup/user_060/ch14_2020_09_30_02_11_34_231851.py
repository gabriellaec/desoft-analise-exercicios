import math
def calcula_distancia_do_projetil(v, teta, yo):
    a = (v**2)/(2*g)
    b = 1 + (1 + (2*g*yo)/(v**2)*(math.sin(teta))**2)**1/2
    c = math.sin(2*teta)
    return a*b*c