import math
g=9.8
a=(v**2)/2*g
b=math.sin(2*theta)
c=math.sqrt(1+((2*g*y0)/math.sin(theta)**2))
def calcula_distancia_do_projetil(a,b,c):
    d=a*(1+c)*b
    return d
