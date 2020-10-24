import math

def reflexao_total_interna (n1, n2, θ2):
    math.sin(θ1) = math.asin((((math.sin(math.radians(θ2))) * n2))/ n1)
    if math.sin(θ1) > 1:
        return True
    else:
        return False
