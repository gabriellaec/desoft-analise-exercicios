import math

reflexao_total_interna = True
def reflexao_total_interna (n1, n2, θ2):
    θ1 = (((math.sin(math.radians(θ1))) * n2))/ n1
    seno_θ1 = math.sin(θ1)
    if math.sin(θ1) > 1:
        return True
    else:
        return False
