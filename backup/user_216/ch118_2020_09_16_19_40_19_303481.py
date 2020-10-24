import math
def reflexao_total_interna(n1,n2,o2):
    return math.sin(math.radians(o2)) > math.sin(n1 / n2)