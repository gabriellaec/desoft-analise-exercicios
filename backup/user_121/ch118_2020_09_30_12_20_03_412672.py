import math
def reflexao_total_interna(n1, n2, θ2):
    θ=math.asin(math.sin(math.radians(θ2))*n2/n1)
    if 2*math.sin(θ)>1:
        resultado=True
    else:
        resultado=False
    return resultado