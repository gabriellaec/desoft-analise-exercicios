import math
def reflexao_total_interna(n1, n2, θ2):
    sinθ1 = math.degrees((n2*math.sin(math.radians(θ2)))/n1)
    if sinθ1>1:
        return True
    else:
        return False