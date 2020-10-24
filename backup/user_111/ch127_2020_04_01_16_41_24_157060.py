import math
def calcula_elongacao(A,ϕ0,w,t):
    elongacao=A*math.radians(math.degrees(math.cosϕ0+(w*t)))
    return elongacao