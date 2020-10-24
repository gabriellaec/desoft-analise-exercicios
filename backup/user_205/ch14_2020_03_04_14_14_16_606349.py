import math
 
def calcula_distancia_do_projetil (v,θ,y):
    g = 9.8
    A = ((v**2)/(2*g))*math.sin(2*θ)
    B = (1 + math.sqrt(1+(2*g*y)/(v**2 * (math.sin(θ))**2)
    
    return (A*B)
    