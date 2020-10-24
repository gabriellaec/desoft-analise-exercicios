import math
def reflexao_total_interna(n2,n1,θ2):
    θ1=(math.asin((n1*math.sin(math.radians(θ2)))/n2))
    if math.sin(θ1)>1:
        r=True
    else:
        r=False
    return  r