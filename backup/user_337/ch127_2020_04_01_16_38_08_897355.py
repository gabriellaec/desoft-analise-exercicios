import math
def calcula_elongacao(a,b,c,t):
    x = a*math.cos(math.radians(b)+math.radians(c)*t)
    return x
    