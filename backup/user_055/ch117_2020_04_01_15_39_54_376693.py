import math
def snell_descartes(n1, n2, θ1):
    c = (math.sin(math.radians(θ1)) * n1)/n2
    s = math.asin(c)
    θ2 = math.degrees(s)
    return θ2