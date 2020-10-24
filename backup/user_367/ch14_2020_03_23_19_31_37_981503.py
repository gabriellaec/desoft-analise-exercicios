import math
def calcula_distancia_do_projetil(v,g,y0):
    d = (v**2/2*g)
    x = (1+(math.sqrt(1+2*g*y0/v**2*(math.sin(0))**2)))
    y = (math.sin(2*0))
    r = d * x * y
    return r