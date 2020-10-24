import math
g = 9.8
def calcula_distancia_do_projetil(v,ang,y0):
    eq1= (v ** 2) / (2 * g)
    eq2=(1 + math.sqrt(1 + (2 * g * y0) / ((v ** 2) * (math.sin(ang)) ** 2) ))
    eq3 = math.sin(2 * ang)
    d = eq1 * eq2 * eq3
    return d