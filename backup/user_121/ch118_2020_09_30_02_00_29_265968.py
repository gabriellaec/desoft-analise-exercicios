import math
def reflexao_total_interna(n1, n2, θ2):
    θ1=math.degrees(math.asin(math.sin(θ2)*n2/n1))
    if sin(θ1)>1:
        resultado=True
    else:
        resultado=False
    return resultado