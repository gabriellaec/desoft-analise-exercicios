import math 

def reflexao_total_interna(n1, n2, θ2):
    a = (n2/n1)*math.sin(math.radians(θ2))
    if a > 1:
        return True
    else: 
        return False