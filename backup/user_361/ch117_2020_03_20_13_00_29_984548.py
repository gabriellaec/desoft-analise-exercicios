import math

def snell_descartes(n1, n2, θ1):
    θ2 = math.arcsin(n1*math.sin(θ1)/n2)
    return θ2