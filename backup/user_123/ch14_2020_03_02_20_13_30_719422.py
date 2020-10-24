import math

def calcula_distancia_do_projetil(v,teta,y):
    g = 9.8
    part1 = ((v ** 2)/(2*g))* (math.sin (2 * teta))
    part2 = (1 + ( 1 + ((2 * g * y) / ((v ** 2) * (math.sin (teta) ** 2)) ** (1/2))))
    part3 = part1 * part2
    return (part3)