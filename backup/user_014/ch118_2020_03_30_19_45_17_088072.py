import math
def reflexao_total_interna (n1, n2, θ2):
    math.sin(θ1) = ((math.sin(math.radians(θ1))) * n1)/ n2
    if math.sin(θ1) > 1:
        reflexão_total_interna = True
    else:
        reflexão_total_interna = False
