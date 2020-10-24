import math
g=9.8
def calcula_distancia_do_projetil(v,θ,y0):
    d=v**2/2*g
    o=(2*g*y0)/v**2*((math.sin(θ))**2)
    f=1+math.sqrt(1+o)
   
    l=math.sin(2*θ)
    k=d*f*l
    return k