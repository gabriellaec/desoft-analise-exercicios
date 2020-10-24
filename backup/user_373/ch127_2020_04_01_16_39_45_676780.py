import math 
def calcula_elongacao(a, o, w,t):
    x= a* math.cos(math.degress(o)+ w*t)
    return x