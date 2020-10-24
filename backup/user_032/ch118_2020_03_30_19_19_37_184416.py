def reflexao_total_interna(n1,n2,θ2):
    import math
     x = (math.sin(math.radians(θ2))*n2)/n1
    if x > 1:
        return True
    else:
        return False
