import math
def calcula_elongacao(A,ϕ0,ω,t):
    ϕ0_em_radianos=ϕ0*(math.pi/180)
    return(A*math.cos(ϕ0_em_radianos+ω*t))