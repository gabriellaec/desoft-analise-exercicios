import math
def calcula_distancia_do_projetil(v,y,z):
    d=((v**2)/(2*9.8))*(1+(1+(2*9.8*y)/((v**2)*((math.sin(y))**2)*math.sin(2*y))
    return d
                           
 