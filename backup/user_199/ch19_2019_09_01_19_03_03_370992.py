import math
def calcula_distancia_do_projetil(v,y0,t,g):
    d=(v**2/2*g)*(1+(1+(2*g*y0/v**2*(math.sin(t))**2)**0.5))*math.sin(t*2)
    return d
v=2
y0=3
t=45
g=9.8
print (calcula_distancia_do_projetil(v,y0,t,g))