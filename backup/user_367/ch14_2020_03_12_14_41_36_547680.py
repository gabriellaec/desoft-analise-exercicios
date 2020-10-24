import math
def calcula_distancia_do_projetil(v,g,y0):
    d = v**2/2*9.8
    x = 1+(math.sqrt(1+2*9.8*y0/v**2*(math.sin(0))**2))
    y = math.sin(20)
    r = d * x * y
    return r