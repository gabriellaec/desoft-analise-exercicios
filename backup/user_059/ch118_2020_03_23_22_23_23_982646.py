import math

def reflexao_total_interna(n1, n2, ang2):
    return (n2*math.sin(math.radians(ang2)/n1)>1)