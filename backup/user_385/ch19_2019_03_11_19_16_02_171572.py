import math
def calcula_distancia_do_projetil(v,a,y):
    d= ((v**2)/2*9.8)*(1+(1+(2*9.8*y)/(v**2)*(math.sin*(a))**2))**(0.5)*math.sin*(2*a)
    return d               