import math
def calcula_elongacao(A,ϕ0,w,t):
    elongacao=A*math.degree(math.cos(ϕ0+w*t))
    return elongacao