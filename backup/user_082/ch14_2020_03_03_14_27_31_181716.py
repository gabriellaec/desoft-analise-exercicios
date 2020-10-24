import math
def calcula_distancia_do_projetil (v, o, h):
    part1= (v**2 / 2*9.8)
    
    part2= (1 + (1 + (2*9.8*h) / (v**2) * (math.sin(o))**2)**(0.5))
    
    part3= (math.sin(2*o))

    return (part1*part2*part3)