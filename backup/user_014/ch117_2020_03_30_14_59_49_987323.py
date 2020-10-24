import math
def snell_descartes (n1, n2, θ1):
    θ2 = (n1 * math.sin(θ1))/ n2
    return math.degrees(math.asin(math.sin(θ2)))

