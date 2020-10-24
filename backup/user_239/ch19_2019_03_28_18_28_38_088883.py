import math
def calcula_distancia_do_projeto(v,a,y):
    d=((v**2)/2g)*(1+(1+(2*9.8*y)/(v**2)*(math.sin(a))**2)**0.5))*math.sin(2*a)
    return d