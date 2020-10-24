import math
def snell_descartes(n1,n2,θ1):
    senθ2 = n1*math.sin(math.radians(θ1))/n2
    θ2 = math.degrees(math.asin(senθ2))
    return θ2