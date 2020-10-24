import math
def calcula_distancia_do_projetil(v,t,y):
    d = ((v**2)/(2*9.8)) * (math.sin(2*t)) * (1+(1+(2*9.8*y)/(v*math.sin(t))**2)**(1/2))
    v = 2
    t = 2
    y = 2
    return d
