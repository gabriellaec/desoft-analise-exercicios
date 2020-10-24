import math
def reflexao_total_interna(n1,n2,θ2):
    θ2 = math.radians(θ2)
    if n2 > n1:
        sen_1 = (math.sin(θ2)*n2)/n1
        if sen_1 > 1:
            return True
        if sen_1 < 1:
            return False