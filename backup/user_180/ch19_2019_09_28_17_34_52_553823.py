def calcula_distancia_do_projetil(v, teta, y0):
    import math
    a = ((v**2)/(2*9.8))
    f = math.sin(math.radians(2*teta))
    b = (2*9.8)*y0
    c = (v**2)*((math.sin(math.radians(teta)))**2)
    return a * (1 + ((1 + (b/c))**0.5)) * f 