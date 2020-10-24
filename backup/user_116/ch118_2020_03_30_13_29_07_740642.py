import math
def reflexao_total_interna(n1,n2,θ2):
    θ1=math.degrees(math.asin(n2*(math.sin(math.radians(θ2)))/n1)
    if θ1<=90:
        r=False
    else:
        r=True
    return  r
