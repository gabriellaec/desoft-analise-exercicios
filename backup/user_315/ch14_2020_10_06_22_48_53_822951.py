import math
g = 9.8
def calcula_distancia_do_projetil(v,teta,y0):
    a = 1 + (1+(2*g*y0)/((v**2)*math.sin(teta)**2))**0.5
    d = ((v**2)/2*g)*a*math.sin(2*teta)
    return d