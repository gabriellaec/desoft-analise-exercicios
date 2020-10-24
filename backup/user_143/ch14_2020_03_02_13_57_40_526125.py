import math
#calcula_distancia_do_projetil
def calcula_distancia_do_projetil (v, b, y0):
    A = ((v**2)/(2*9.8))
    J = ((1) + (math.sqrt(1 + ((2*9.8*y0)/((v**2)*(math.sin(b))**2)))
    d = A * J * math.sin(2*b)
    return d
                                      
                                      