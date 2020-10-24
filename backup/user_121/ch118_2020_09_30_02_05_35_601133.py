import math
def reflexao_total_interna(n1, n2, θ2):
    dale=math.sin(θ2)*n2/n1
    θ=math.sin**-1(dale)
    if math.sin(θ)>1:
        resultado=True
    else:
        resultado=False
    return resultado