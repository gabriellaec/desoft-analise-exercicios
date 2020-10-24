import math
def calcula_distancia_do_projetil (v,a,h):
    raiz = math.sqrt (1+((2*9.8*h)/(v**2)*(math.sin(a))**2))
    distancia = ((v**2)/(2*9.8))*(1 + raiz)*(math.sin(a*2))
    return distancia
                              
   