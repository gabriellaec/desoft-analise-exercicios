
import math
def calcula_distancia_do_projetil(v,θ,y0):
    g=9.8
    a=(v**2)/2*g
    b=2*g*y0
    c=(v**2)*(math.sin(θ)**2)
    d=(1+b/c)**0.5
    R=a*(1+d)*math.sin(2*θ)
    return R