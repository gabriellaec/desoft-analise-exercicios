import math 
def calcula_distancia_do_projetil (v,θ,y0):
    a= v/(2*9.8)
    b= 1
    c= (1+ (2*9.8*y0)/(v**2)(math.sin(θ)**2)
    d=math.sin*(2*θ)
    e = a*(b+c)*d
    return e