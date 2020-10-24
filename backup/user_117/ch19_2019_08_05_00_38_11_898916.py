import math
def calcula_distancia_do_projetil(v, g, y0, t):
    g = 9.8
    a = (v ** 2)/(2 * g)
    b = 1 + ((2 * g * y0) / (v**2) * (math.sin(t))**2           
             
    d = a * (1 + (math.sqtr(b))) * math.sin(2 * t)
    return d
             