import math as m

def calcula_elongacao(A, ϕ, ω, t):
    x = A * m.cos(m.radians(ϕ + ω * t ))
    return x