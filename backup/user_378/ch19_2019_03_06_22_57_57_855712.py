import math
def calcula_distancia_do_projetil(v,teta,y0):
    y=v**2/19.6*(1+(1+19.6*y0/(v**2*(math.sin(teta))**2))**(1/2))*math.sin(2*teta)
    return y