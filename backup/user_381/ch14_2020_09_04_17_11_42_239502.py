import math
def calcula_distancia_do_projetil(v,θ,y):
    a = (v**2)/2*9.8
    b = (2*9.8*y)/(v**2*(math.sin(θ)**2))
    c = math.sin(2*θ)**2
    d = a*(1+(1+b)**(1/2))*c    
    return d