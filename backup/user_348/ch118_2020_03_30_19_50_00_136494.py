import math
def reflexao_total_interna (n1,n2,θ2):
    sin(θ1) = (n2*math.sin(θ2))/n1
    if sin(θ1) > 1:
        return reflexao_total_interna = True 
    else:
        return reflexao_total_interna = False 