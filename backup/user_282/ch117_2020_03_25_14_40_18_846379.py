import math
def snell(n1, θ1, n2):
    θ2 = math.asin((n1*math.sin(θ1))/n2)
    return θ2
