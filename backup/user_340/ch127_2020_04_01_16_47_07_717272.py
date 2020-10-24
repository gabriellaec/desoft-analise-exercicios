import math
def calcula_elongacao(A,y,w,t):
    f=math.radians(y)
    k=(w*t)
    j=math.radians(k)
    i=(f+j)
    x=A*(math.cos(i))
    return x