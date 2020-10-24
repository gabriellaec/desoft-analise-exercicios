
import math

g=9.8
def calcula_distancia_do_projetil(g,theta,v,y0):
    a=(v**2)/2*g
    b=math.sin(2*theta)
    c=math.sqrt(1+((2*g*y0)/(v**2)*math.sin(theta)**2))
    d=a*(1+c)*b
    return d
