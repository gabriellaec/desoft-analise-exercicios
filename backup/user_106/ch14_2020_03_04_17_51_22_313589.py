import math
a=(v**2)/19.6
b=1
c=1+(19.6*y)/((v*math.sin(θ))**2)
d=math.sin(2*θ)
def calcula_distancia_do_projetil(v,θ,y):
    y=a*(b+c)*d
    return y