import math
def calcula_distancia_do_projetil (v,y,a)
    d=((v**2)/2*9.8)*(1+((1+(2*9.8*y))/(v**2)*(math.sin(a))**2))**1/2*(math.sin(2a))
    return d