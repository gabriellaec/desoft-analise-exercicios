import math
def reflexao_total_interna (n1,n2,θ2):
    θ1 = math.asin((n2*math.sin(θ2))/n1)
    if θ1 <= math.pi:
        return reflexao_total_interna = False
    else:
        return reflexao_total_interna = True