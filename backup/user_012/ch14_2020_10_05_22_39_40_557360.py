import math
def calcula_distancia_do_projetil(v, teta, yo):
    a= (v**2/2*9.8)
    b= (1+(1+((2*9.8*yo)/(v**2)*(math.sin*(teta))**2))**0.5)
    c= math.sin(2*teta)
    return a*b*c

