import math
def calcula_distancia_do_projetil (v , y , z):
    m = (v**2) / (2*9.8)
    t = (1 + (2*9.8*y / v**2 * (math.sin(y)**2)))**0.5
    j = m * (1 + t) * math.sin(2 * y) 
    return j
    