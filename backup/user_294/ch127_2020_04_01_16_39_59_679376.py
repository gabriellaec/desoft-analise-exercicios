import math
def calcula_elongacao(A,ϕ,ω,t):
    ϕ=math.radians(ϕ)
    x=A*(math.cos((ϕ)+(ω*t)))
    return x