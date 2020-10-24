import math 
def calcula_elongacao(a, o, w,t):
    x= a* math.cos(math.radians(o+ w*t))
    y=math.acos(o+ w*t)
    return y