import math
def calcula_distancia_do_projetil(v, teta, yo):
    d= (v**2/2*9.8)*(1+(1+2*9.8*yo/v**2*(math.sin*(teta))**2)**0.5)*math.sin(2*teta)
    return d