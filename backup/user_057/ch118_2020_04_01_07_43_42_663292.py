import math

def reflexao_total_interna(n1,n2,θ2):
    θ2=math.radians
    Senoθ1=(n2*math.sin(θ2))/n1
    if Senoθ1 > 1:
        return true
    else:
        return false