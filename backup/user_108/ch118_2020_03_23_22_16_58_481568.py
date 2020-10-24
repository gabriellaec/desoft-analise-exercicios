import math

def reflexao_total_interna(n1,n2,a2):
    return !(math.degrees(n2 * math.sin(math.radians(a2)) / n1) > 1)
