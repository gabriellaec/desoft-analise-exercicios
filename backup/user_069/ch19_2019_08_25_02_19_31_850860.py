def calcula_distancia_do_projetil (v,o,y0):
    import math
    d = (v**2/2*9.8)*(1 + (1 + (2*9.8*y0/v**2*math.sin(o)**2))**0.5)*math.sin(2*o)
    return d