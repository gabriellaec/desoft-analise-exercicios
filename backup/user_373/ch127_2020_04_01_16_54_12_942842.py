import math 
def calcula_elongacao(a, o, w,t):
    x= a* math.cos(math.radians(o)+ math.radians(w)*t)
    y=math.acos(x)
    return x