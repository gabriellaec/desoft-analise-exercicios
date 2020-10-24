import math
def calcula_distancia_do_projetil(v,θ,yo):
    g=9.8
    A=(v**2)/(2*g)
    B=(2*g*yo)/(v**2*(math.sin(θ)**2))
    d=A*(1+(1+B)**(1/2))*math.sin(2*θ)
    return d