from math import sin, asin, radians, degrees

def reflexao_total_interna(n1,n2,θ2):
    teta = sin(radians(θ2)) * n1 / n2
    teta1 = degrees(asin(teta))
    if sin(degrees(teta1)) > 1:
        return True   
    else:
        return False
    