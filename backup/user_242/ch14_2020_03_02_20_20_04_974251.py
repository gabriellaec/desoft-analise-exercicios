import math
g=9.8
def calcula_distancia_do_projetil(v,g,y,teta):
    D = v**2/2*g*(1+(1+2*g*y/v**2*(math.sin(teta)))**1/2)*math.sin(2*teta)
    return D