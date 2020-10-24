import math
def calcula_elongação(a,b,c,t):
    x=a*(math.cos(math.radians(a)+math.radians(c)*t))
    return x