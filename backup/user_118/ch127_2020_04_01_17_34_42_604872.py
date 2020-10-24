import math
def calcula_elongacao(A,o,w,t):
    x=A*math.acos(math.radians(o)+(w*t))
    return (math.degrees(x))
