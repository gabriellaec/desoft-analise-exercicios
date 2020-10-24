import math
def reflexao_total_interna(n1, n2, θ2):
    y = (math.sin(math.radians(θ2)))*(n2)/(n1)
    x = math.degrees(math.asin(y))
    return x