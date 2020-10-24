import math
def calcula_elongacao(A,o,w,t):
    x=math.degrees(A*math.cos(math.radians(o)+(w*t)))
    return x
