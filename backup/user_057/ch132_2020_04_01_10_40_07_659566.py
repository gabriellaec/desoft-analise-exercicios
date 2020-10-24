import math

def calcula_trabalho(F,θ,s):
    θ= math.radians(θ)
    τ= F*(math.cos(θ))*s
    return τ
