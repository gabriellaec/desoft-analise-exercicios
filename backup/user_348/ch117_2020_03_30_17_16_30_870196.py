import math
def snell_descartes (n1, n2, θ1):
    θ2 = math.asin((n1*(math.sin(math.radians(θ1))))/n2)
  	grau_θ2= math.degrees(θ2)
    return grau_θ2
