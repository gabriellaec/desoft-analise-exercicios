import math
def calcula_distancia_do_projetil (v, teta, y):
    f=(v**2/2*9.8)*math.sin(2*teta)*(1+math.sqrt(1+(2*9.8*y))/(v**2*(math.sin(teta))**2))
    return f
                    

