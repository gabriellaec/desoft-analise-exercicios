import math
def reflexao_total_interna(n1, n2, θ2):
    if (n2 * math.sin(math.radians(θ2)))/n1 > 1:
        r = True
    else:
        r = False
    return r 