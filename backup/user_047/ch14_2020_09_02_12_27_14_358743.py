import math
def calcula_distancia_do_projetil(v,y0,r):
    g = 9.8 
    velocidade = v**2/(2*g)
    gg = 2*g*y0
    vx = v**2*math.sin(r)**2
    d = velocidade*(1+math.sqrt(1+gg/vx))
    return d