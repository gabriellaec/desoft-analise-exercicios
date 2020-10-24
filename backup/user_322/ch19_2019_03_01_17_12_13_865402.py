import math
def calcula_distancia_do_projetil(v, x, k):
    y = ((v ** 2)/2 * 9,8) * (1 + ((1 + (2 * 9,8 * k )/(v ** 2 * (math.sin(x)) ** 2)))**(1/2)) ** math.sin(2*x)
    return y
    