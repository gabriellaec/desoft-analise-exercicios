import math
def calcula_elongacao(A,ϕ,ω,t):
    x=A*(math.cos(ϕ+(ω*t)))
    return x