import math
def calcula_distancia_do_projetil(v,b,y):
    return (v**2/2*g)*(1+(1+(2*g*y)/(v**2*(math.sin(b))**2))**(1/2)*math.sin(2*b)