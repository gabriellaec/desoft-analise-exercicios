import math
def reflexao_total_interna (n1, n2, θ2):
    θ1 = ((math.sin(θ2) * n2))/ n1
    seno_θ1 = math.sin(θ1)
    if seno_θ1 > 1:
        return True
    else:
        return False