import math
def snell_descartes (n1,n2,teta1):
    θ2= math.degrees(math.asin(math.asin(math.radians (teta1)) * n1/n2))
    return θ2
