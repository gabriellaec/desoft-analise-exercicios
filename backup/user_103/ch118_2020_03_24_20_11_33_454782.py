import math
def reflexao_total_interna(n1, n2, θ2):
    θ2=math.radians(θ2)
    θ1=((n2*math.sin(θ2))/n1)
    if math.sin(θ1)>1:
        return True
    else:
        return False