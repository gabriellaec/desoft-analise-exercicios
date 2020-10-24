import math
def calcula_distancia_do_projetil(v,y0):
    g = 9.8 
    velocidade = (v**2)/2*g
    gg = 2*g*y0
    vx = v**2(math.sin(30)**2)
    d = velocidade*(1+(gg+1/vx)**1/2)
    return d
x = calcula_distancia_do_projetil(5,10)