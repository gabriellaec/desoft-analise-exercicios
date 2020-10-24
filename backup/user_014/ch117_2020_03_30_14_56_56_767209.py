import math
def snell_descartes (n1, n2, θ1):
    θ2 = (n2 * math.asin(θ1))/ n1
    return math.degrees(math.asin(math.sin(θ2)))

