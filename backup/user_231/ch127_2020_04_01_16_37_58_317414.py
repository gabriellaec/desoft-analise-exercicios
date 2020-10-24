import math
def calcula_elongacao(A,ϕo,w,t):
    x= A*math.cos(ϕo+w*t)
    return x
