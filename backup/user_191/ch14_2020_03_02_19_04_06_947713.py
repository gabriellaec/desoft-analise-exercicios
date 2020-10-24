import math
def calcula_distancia_do_projetil(v,yo,j):
    a=v**2
    b=2*9.8
    c=(1+(2*9.8*yo)/((v**2)*(math.sin(j)**2))**1/2
    d=a/b*(1+c)*math.sin(2*j)
    return d
print(calcula_distancia_do_projetil(2,2,2))