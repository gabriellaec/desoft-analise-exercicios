import math
def snell_descartes (n1, n2, θ1):
    θ2 = math.asin((n1*(math.sin(θ1*math.pi/180)))/n2)
    k=(180*θ2)/math.pi
    return k
