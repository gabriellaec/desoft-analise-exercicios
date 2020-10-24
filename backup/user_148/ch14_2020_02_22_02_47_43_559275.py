import math

def calcula_distancia_do_projetil(v, o, y0):
    d = ((v**2)*(math.sin(2*o))*(1+(1+((2*9.8*y0)/(v**2)*(math.sin(0))**(1/2)))**(1/2)))/(2*9.8)
    return d