import math
def calcula_distancia_do_projetil (v,T,y):
    d=(v**2/2*9.8*y)*(1+((1+(2*9.8*y))/(v**2)*(math.sin(a))**2)**(1/2))*(math.sin(2*T))
    return d