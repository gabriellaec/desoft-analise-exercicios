from math import sin, radians

def reflexao_total_interna(n1,n2,θ2):
    teta = sin(radians(θ2)) * n1 / n2
    if sin(teta) > 1:
        return True   
    else:
        return False
    