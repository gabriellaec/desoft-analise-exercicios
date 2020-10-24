import math
def	calcula_distancia_do_projetil(v,O,y0):
    return (v**2/19.6)*(1+(1+((2*9.8*y0)/(v**2)*math.sin*(O))**0.5))*math.sin*(2*O)