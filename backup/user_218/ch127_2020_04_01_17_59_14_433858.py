# a = amplitude do movimento (em metros)
# o = fase inicial da partícula (em graus)
# w = velocidade agular (em graus por segundo) --- w = v / r
# t = tempo (em segundos) 
# elongação (em metros)

import math
def calcula_elongacao(a, o, w, t):
    k = math.radians(o)
    l = (w * t)
    m = math.radians(l)
    n = (k + m)
    x = a * (math.cos(n))
    return x

