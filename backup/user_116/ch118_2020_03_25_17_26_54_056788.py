import math
def reflexao_total_interna(n1,n2,θ2):
    θ1=(math.degrees(math.asin((n2*math.sin(math.radians(θ2)))/n1)))
    if math.sin(math.radians(θ1))>1:
        r=True
    else:
        r=False
    return  r