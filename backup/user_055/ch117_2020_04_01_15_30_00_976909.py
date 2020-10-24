import math
def snell_descartes(n1, n2, θ1):
    c = (math.sin(math.degrees(θ1)) * n1)/n2
    θ2 = math.sin(math.degrees(c))
    return θ2