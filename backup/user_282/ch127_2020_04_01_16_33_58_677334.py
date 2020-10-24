import math as m

def calcula_elongacao(A, ϕ, ω, t):
    x = A * m.cos(ϕ + ϕ * t )
    return x