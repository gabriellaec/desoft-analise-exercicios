import math

def reflexao_total_interna(n1,n2,a2):
    return not (math.degrees(n1 * math.sin(math.radians(a2)) / n2) > 1)
