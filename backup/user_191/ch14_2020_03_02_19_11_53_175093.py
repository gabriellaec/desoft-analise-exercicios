import math
def calcula_distancia_do_projetil(v,yo,j):
    a=v**2
    b=2*9.8
    c=(1+(2*9.8*yo)/((v**2)*(math.sin(j)**2)))**0.5
    d=math.sin(2*j)
    e=a/b(1+c)*d
    return e
print(calcula_distancia_do_projetil(1,1,1))