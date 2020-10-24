import math

def calcula_distancia_do_projetil(v, h, y):
    p1 = v ** 2 / (2 * 9.8) 
    p2 = 2 * 9.8 * y
    p6 = math.sin(h)
    p3 = v ** 2 * p6 ** 2
    p7 = 1 + p2 / p3
    p4 = 2 * h
    p5 = math.sin(p4)
    distancia = p1 * (1 + math.sqrt(p7)) * p5 
    return distancia                  
                    
                      