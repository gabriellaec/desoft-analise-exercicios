import math
def calcula_distancia_do_projetil(v,θ,yo):
    d=(v**2/(2*9.8))*math.sin(2*θ)*(1+(((v*math.sin(θ)**2)+2*9.8*yo))**0.5)/(v*math.sin(θ))
    return d
a=10
b=1
c=0
z= calcula_distancia_do_projetil(a,b,c)
print(z)