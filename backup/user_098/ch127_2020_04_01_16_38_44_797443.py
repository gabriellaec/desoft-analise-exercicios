import math

def calcula_elongacao(A,Fi,w,t):
    Fi = math.radians(Fi)
    w = math.radians(w)
    return A*math.cos(Fi + w*t)