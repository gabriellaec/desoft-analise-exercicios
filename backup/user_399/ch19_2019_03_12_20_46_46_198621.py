import math
def calcula_distancia_do_projetil(v,y0,a):
    d=(v**2/2*g)*math.sin(2*a)*(1+math.sqrt(1+(2*g*y0)/((v**2)*(math.sin(a))**2)))
    return d
g=9,8