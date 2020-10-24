import math
def calcula_elongacao(A,y,w,t):
    t=math.radians(y)
    k=(w*t)/t
    j=math.radians(k)
    i=(t+j)
    x=A*(math.cos(i))
    return x