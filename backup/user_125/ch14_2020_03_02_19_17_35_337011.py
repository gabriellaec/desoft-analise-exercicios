import math 

def calcula_distancia_do_projetil (v,θ,yθ):
    d= ((v**2)/2*9.8)*(1+(1+(2*9,8*yθ))/(v**2)*(math.sin)*θ**2)*math.sin(2*θ)
    return d 
