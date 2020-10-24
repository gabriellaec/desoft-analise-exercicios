import math

def calcula_distancia_do_projetil(v, h, y):
    p1 = v ** 2 / (2 * 9.8) 
    p2 = 2 * 9.8 * y
    p3 = v ** 2 * (math.sin(h)) ** 2
    p4 = 2 * h
    p5 = math.sin(p4)
    distancia = p1 * (1 + math.sqrt(1 + (p2 / p3)) * p5 
    return distancia                  
                    
                      