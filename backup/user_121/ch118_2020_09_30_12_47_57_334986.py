import math
def reflexao_total_interna(n1, n2, θ2):
    if math.sin(math.radians(θ2))*n2/n1 > 1:
        resultado=True
    else:
        resultado=False
    return resultado