import math
def calcula_distancia_do_projetil(v,g,yo,j):
    d=v**2/2*g*(1+(1+2*g*yo/v**2*(math.sin(j))**2)**0.5)*math.sin(2*j)
    return d
print(calcula_distancia_do_projetil(2,2,2,2))