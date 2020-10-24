import math 
def calcula_distancia_do_projetil(v, an, y):
    g = 9.8
    a = v**2/(2*g) 
    b = 1 + math.sqrt(1+2*g*y/(v**2 * math.sin(an)**2))
    c = math.sin(2*an)
    z = a*b*c
    return z