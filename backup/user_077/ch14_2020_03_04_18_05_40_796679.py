import math
def calcula_distacia_do_projetil(v,θ,y0):
    a=(v**2)/19.6
    b=19.6*y0
    c=(v**2)*(math.sin(θ))**2
    d=math.sin(2*θ)
    calcula_distacia_do_projetil=a*(1+(1+b/c)**1/2)*d
    return calcula_distacia_do_projetil