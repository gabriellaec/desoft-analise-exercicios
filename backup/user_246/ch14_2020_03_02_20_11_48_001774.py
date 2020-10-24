import math
def calcula_distancia_do_projetil(x,y,z):
    d=(x**2)/(2*9.8)*(1+(1+(2*9.8*z)/((x**2)*(math.sin(y)))**2)**-1)*math.sin(2*y)
    return d