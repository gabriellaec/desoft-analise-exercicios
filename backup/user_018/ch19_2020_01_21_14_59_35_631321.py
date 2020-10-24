from math import sqrt,sin
def calcula_distancia_do_projetil (v,teta,y0):
    d = ((v**2)/2*9.8) *1 + sqrt((1+((2*9.8*y0)/((v**2)*sin(teta)**2)))) * sin(2*teta)
    return d 