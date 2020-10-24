import math
g=9.8
def calcula_distancia_do_projetil(v,O,y):
    d=(v**2/2*g)*(1+math.sqrt(1+(2*g*y/v**2(math.sin(O))**2)))*math.sin(2*O)
    return d