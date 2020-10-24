import math
g=9.8
def calcula_distancia_do_projetil(v,y0,g,theta):
    d=((v**2)/2*g)*(1+math.sqrt(1+((2*g*y0)/((v**2)*(math.sin(theta))**2))))*math.sin(2*theta)
    return d
