import math
def calcula_elongacao(A,ϕo,w,t):
    a=math.radians(ϕo)
    b=math.radians(w)
    c=math.cos(a+b*t)
    x= A*c
    return x
