import math
g= 9.8
def calcula_distancia_do_projetil(v, y0, angulo):
    d= (((v)**2)/(2*g))*(1 + (1 + (2*g*y0)/(v)**2(math.sin(angulo))**2))*math.sin(2*angulo)
    return d 
a=3
b=10
c=30
r=calcula_distancia_do_projetil(a, b, c)
print(r)