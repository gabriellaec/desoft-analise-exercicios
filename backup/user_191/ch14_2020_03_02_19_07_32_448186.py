import math
def calcula_distancia_do_projetil(v,yo,j):
    d=(v**2)/(2*9.8)*(1+(1+(2*9.8*yo)/((v**2)*(math.sin(j)**2)))**0.5)*(math.sin(2*j))
    return d
print(calcula_distancia_do_projetil(2,2,2))