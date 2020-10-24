import math
def calcula_elongacao(A,ϕ,ω,t):
    ϕ=(math.radians(ϕ))
    b=((ϕ)+(ω*t))
    x=A*(math.cos(b))
    return x