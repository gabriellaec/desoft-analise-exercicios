import math
def calcula_distancia_do_projetil(v,O,y0):
    g=9.8
    a=((v**2)*(math.sin(2*O)))/(2*g)
    b=1+((2*g*y0)/((v**2)*((math.sin(O))**2)))
    distancia=a*b
    return distancia