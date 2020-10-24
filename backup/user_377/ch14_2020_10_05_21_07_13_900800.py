import math
g=9.8
a= v**2/2*g
b=(1 + (2*g*y0)/v**2 * (math.sin(θ))**2)**1/2
def calcula_distancia_do_projetil(v, θ, y0):
    dp=a*(1+b)* math.sin(2*θ)
    return dp
