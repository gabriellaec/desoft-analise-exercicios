import math 
g=9.8

def calcula_distancia_do_projetil(v,t,y0):
    T = math.radians(t)
    D=((v**2)/2*g)*(1+((1+((2*g*y0)/(v**2)*(math.sin(T)**2)))**(1/2)))*math.sin(2*T)
    return D

A=calcula_distancia_do_projetil(5,(math.pi/6),10)

print(A)