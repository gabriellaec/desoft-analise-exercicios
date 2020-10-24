import math
def calcula_distancia_do_projetil(v,yo,j):
    a=(v**2)/(2*9.8)
    b=((2*9.8*yo)/(v**2*(math.sin(j))**2))**0.5
    d=a*(1+b)*math.sin(2*j)
    return d
print(calcula_distancia_do_projetil(2,2,2))