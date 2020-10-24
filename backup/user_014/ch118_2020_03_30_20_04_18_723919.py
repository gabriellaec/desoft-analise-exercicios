import math
def reflexao_total_interna (n1, n2, θ1):
    θ1 = (((math.sin(math.radians(θ1))) * n1))/ n2
    seno_θ1 = math.sin(θ1)
    if seno_θ1 > 1:
        return True
    else:
        return False