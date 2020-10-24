import math
g=9.8
def calcula_distancia_do_projetil(v,teta,y):
    distancia=(v**2/2*g)*math.sin(2*teta)*(1+ math.sqrt(1+(2*g*y)/(v**2*(math.sin(2*teta))**2)
    return distancia                              
                                                       