import math
def calcula_distancia_do_projetil(v,θ,yo):
    d=(((v**2)*math.sin(2*θ))/2*9.8)*(1+(1+(2*9.8*yo)/((v*math.sin(θ))**2))**0.5)
    return d
a=10
b=1
c=0
z= calcula_distancia_do_projetil(a,b,c)
print(z)