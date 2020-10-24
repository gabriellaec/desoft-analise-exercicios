import math

def calcula_distancia_do_projetil(v,t,y):
    g = 9.8
    tmp1 = (v**2)/(2*g)
    tmp2 = 1 + (1 + math.sqrt((2 * g * y)/(v**2) * (math.sin(t)**2)))
    tmp3 = math.sin(t * 2)
    return tmp1 * tmp2 * tmp3