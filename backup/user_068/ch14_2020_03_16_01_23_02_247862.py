import math
g= 9.8
def calcula_distancia_do_projetil(v, angulo, altura):
    d = ((v**2)/(2*g))*(1 + math.sqrt(1+ ((2*g*altura)/((v**2)*(math.sin(angulo)
    return d
a=10
b=7
c=5
r = calcula_distancia_do_projetil(a, b, c)
print(r)