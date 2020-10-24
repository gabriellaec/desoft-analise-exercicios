import math
def calcula_distancia_do_projetil(v,A,yo):
    return  (v**2) * (1 + (math.sqrt(1 + (2 * 9.8 * yo)/((v**2) * ((math.sin(A))**2))))) * (math.sin(2*A))/(2 * 9.8)