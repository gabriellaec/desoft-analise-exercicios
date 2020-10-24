import math
def snell_descartes (n1, n2, θ1):
    θ2 = (n2 * math.sin(θ1))/ n1
    return math.degrees(math.sin(θ2))

