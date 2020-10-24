import math 
def calcula_elongacao(a, o, w,t):
    x= a* math.cos(math.degrees(o)+ w*t)
    return x