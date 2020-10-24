import math
g=9.8
def calcula_distancia_do_projetil(v,θ,h):
    a=(v**2)/(2*g)
    b=1+math.sqrt(1+(2*g*h)/((v*(math.sin(math.degrees(θ))))**2)
    c=math.sin(2*(math.degrees(θ)))
    d=a*b*c
    return d