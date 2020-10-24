import math
def reflexao_total_interna(n1, n2, θ2):
    θ=math.sin(math.radians(θ2))*n2/n1
    if math.sin(θ)<1:
        resultado=False
    else:
        resultado=True
    return resultado