import math
def	calcula_distancia_do_projetil(v,O,y):
    return (v**2/19.6)*(1+(1+(19.6*y)/(v**2)*math.sin*(O))**0.5)*math.sin*(2*O)