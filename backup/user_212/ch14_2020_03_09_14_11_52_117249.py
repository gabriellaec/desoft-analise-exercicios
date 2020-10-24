from math import sin
def calcula_distancia_do_projetil(v,θ,y0):
    g=9.8
    a=v**2/(2*g)
    b= (1+((1+(2*g*y0)/(v**2*(sin(θ)**2))**0.5)))
    c=sin(2*θ)
    return(a*b*c)
