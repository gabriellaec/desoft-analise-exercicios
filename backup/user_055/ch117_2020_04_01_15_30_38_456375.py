import math
def snell_descartes(n1, n2, θ1):
    c = (math.sin(math.radians(θ1)) * n2)/n1
    θ2 = math.sin(math.degrees(c))
    return θ2