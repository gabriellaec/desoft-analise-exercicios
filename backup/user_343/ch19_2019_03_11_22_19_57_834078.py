import math
g=9.8
def calcula_distancia_do_projetil(v, a, y0):
    y = ((v**2)/(2*(g)))*(1+(1+(2*(g)*y0/(v**2)*(math.sin(a))**2)))*math.sin(2*a)
    return y                  
                      