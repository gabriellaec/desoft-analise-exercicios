import math
def calcula_elongacao(A,ϕ0,w,t):
    elongacao=A*math.degrees(math.radians((math.cos(ϕ0+w*t))))
    return elongacao