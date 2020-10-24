import math
def snell_descartes(n1, n2, θ1):
    c = (math.sin(math.radians(θ1)) * n1)/n2
    θ2 = math.asin(math.degrees(c))
    return θ2