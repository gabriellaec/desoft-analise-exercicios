import math
def calcula_distancia_do_projetil(v,O,y0):
    d=v**2*9,8(1+0.5**(1+(2*9.8*y0)/v**2*(math.sin(O))**2)*math.sin(2*O)
    return d