import math
def calcula_elongacao(A,o,w,t):
    x=A*math.acos(math.degrees(o+w*t))
    return x
