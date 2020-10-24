import math
def calcula_distancia_do_projetil(v, y0, t):
    
    d = ((v**2)/2) * ((1 + (math.sqrt(1 + (2 * 9.8 *y0)/(v**2)*(math.sin(t))**2))))*math.sin(2*t)
    return d