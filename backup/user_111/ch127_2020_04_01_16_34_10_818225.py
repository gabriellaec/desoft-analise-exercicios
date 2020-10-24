import math
def calcula_elongacao(A,ϕ0,w,t):
    elongacao=A*math.cos(ϕ0+w*t)
    return elongacao