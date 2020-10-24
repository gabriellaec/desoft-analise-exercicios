import math
def calcula_distancia_do_projetil(v, teta, y0):
    g = 9.8
    part2 = (1 + (1 +( ((2*g*y0) / ((v**2) * ((math.sin(teta)) **2))))**(1/2)))
    d = ((v**2)/(2*g)) * part2 * (math.sin(2*teta))
    return d