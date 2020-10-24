import math

def calcula_distancia_do_projetil (v,g,y,o):
    distancia = ( v**2 / 2*g )*(1 + math.sqrt( 1 + 2*g*y/v**2 * (math.sin(o))**2)*math.sin(2*o)
    return distancia
    
                                print (calcula_distancia_do_projetil (30,9.8,100,math.pi/3)