import math
def calcula_distancia_do_projetil (v, x , y0):
    d = v**2 / 2 * 9.8 * (1 + pow(1 + 2 * 9.8 * y0 / v**2 *( math.sin(x))**2)) * math.sin(2*x)
    return d
                        