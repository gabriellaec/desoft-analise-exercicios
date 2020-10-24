import math
def reflexao_total_interna(n1,n2,teta2):
    return math.sin(math.radians(teta2)) > math.sin(n1 / n2)
