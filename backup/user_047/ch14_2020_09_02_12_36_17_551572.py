import math
def calcula_distancia_do_projetil(v,a,h):
    g = 9.8 
    velocidade = v**2/(2*g)
    gg = 2*g*h
    vx = v**2*math.sin(a)**2
    z = math.sin(2*a)
    d = velocidade*(1+math.sqrt(1+gg/vx))*z
    return d