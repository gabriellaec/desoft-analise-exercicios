from math import sin, asin, radians, degrees

def reflexao_total_interna(n1,n2,θ2):
    teta = sin(radians(θ2)) * n2 / n1
    teta1 = degrees(asin(teta))
    if teta1 == 0:
        return False
    elif teta1 > θ2:
        return False
    elif teta1 == 90:
        return False
    else:
        return True
    