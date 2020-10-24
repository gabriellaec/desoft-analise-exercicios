import math
def calcula_elongacao(a,b,c,t):
    x=a*(math.cos(math.radians(a)+math.radians(c)*t))
    return x