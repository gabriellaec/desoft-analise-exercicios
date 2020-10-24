import math
def reflexao_total_interna(n1,n2,θ2):
    y = (n2*math.sin(θ2))/n1
    return y
    if y > 1:
        y = True
        return y
    else:
        y = False
        return y
