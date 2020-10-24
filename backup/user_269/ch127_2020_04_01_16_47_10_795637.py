import math
def calcula_elongacao(A,ϕ0,ω,t):
    return(A*math.cos(ϕ0*math.pi/180+ω*t))