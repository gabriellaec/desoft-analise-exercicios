#exercicio14
import math 
g=9.8

def calcula_distancia_do_projetil(v,t,y):
    a=((v**2)/(2*g))
    b=((v**2)*((math.sin(t))**2))
    c=(2*g*y)
    d=((1+(c/b))**(1/2))
    D=(a*(1+d)*math.sin(2*t))
    return D

A=calcula_distancia_do_projetil(5,(math.pi/6),10)

print(A)