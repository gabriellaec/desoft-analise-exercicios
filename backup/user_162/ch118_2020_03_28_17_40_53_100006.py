import math

def reflexao_total_interna(n1, n2, θ1):
    a = (n1/n2)*math.sin(math.radians(θ1))
    if math.sin(a)>1:
        return True
    else:
        return False