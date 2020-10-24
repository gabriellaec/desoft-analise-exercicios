import math
def calcula_distancia_do_projetil (v, t, y0):
    y= (v**2)/(2*9.8) * (1+(1+(2*9.8*y0)**1/2))/((v**2)*(math.sin(t))**2)*(math.sin(t*2))
    return y
    