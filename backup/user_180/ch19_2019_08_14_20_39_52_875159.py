def calcula_distancia_do_projetil(v, teta, y0):
    import math
    d = (v**2/2*10) * (1 + ((1+2*10*y0/v**2 * (math.sin(teta)**2)))**1/2) * (math.sin(2*teta))
    return d

print(calcula_distancia_do_projetil(5, 30, 20))