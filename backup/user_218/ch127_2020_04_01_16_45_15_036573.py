# a = amplitude do movimento (em metros)
# o = fase inicial da partícula (em graus)
# w = velocidade agular (em graus por segundo) --- w = v / r
# t = tempo (em segundos) 
# elongação (em metros)

import math
def calcula_elongacao(a, o, w, t):
    x = a * math.cos (o + w * t)
    y = x * 180 / math.pi
    return y

