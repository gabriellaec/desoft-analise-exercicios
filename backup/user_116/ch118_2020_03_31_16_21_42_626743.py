import math
def reflexao_total_interna (n1, n2, θ2):
    θ1 = math.degrees(math.sin(math.radians (θ2)) * n2 / n1)
    if θ1 > 90:
        return True
    else:
        return False

    

