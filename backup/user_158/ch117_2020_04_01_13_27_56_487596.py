import math
def snell_descartes(n1,n2,θ1):
    θ2R=math.asin((math.sin(math.radians(θ1))*n2)/n1)
    θ2 = math.degrees(θ2R)
    return θ2
    