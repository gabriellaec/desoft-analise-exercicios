import math
g=9.8
def calcula_distancia_do_projetil (v, o, h):
    part1= (v**2 / 2*g)
    part2= 1 + (1 + 2*g*h / v**2 * (math.sin(o))**2)**(1/2)
    part3= math.sin(2*o)
    return (part1*part2*part3)