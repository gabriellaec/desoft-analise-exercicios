import math
def calcula_distancia_do_projetil(v,θ,y0):
    a=(v**2)/19.6
    b=19.6*y0
    c=(v**2)*(math.sin(θ))**2
    d=math.sin(2*θ)
    y=a*(1+math.sqrt(1+(b/c)))*d
    return y