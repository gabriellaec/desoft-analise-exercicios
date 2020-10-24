import math
def calcula_distancia_do_projetil(v,t, y0):
    g = 9.8
    a = (v ** 2)/(2 * g)             
    d = a * (1 + (math.sqtr(1 + ((2 * g * y0) / (v**2) * (math.sin(t))**2))) * (math.sin(2 * t)))
    return d