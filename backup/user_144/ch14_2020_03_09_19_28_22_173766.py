from math import sin, sqrt 
g = 9.8

def calcula_distancia_do_projetil(v,θ,y0):
    
    x = (v**2) / 2*g
    y = (1+sqrt(1+(2*g*y0)/(v**2*(sin(θ))**2)))
    z = sin(2*θ)
    f = x*y*z
    
    return f 
