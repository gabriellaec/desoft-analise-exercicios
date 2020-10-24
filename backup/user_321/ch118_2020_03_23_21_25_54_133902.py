import math
def reflexao_total_interna(n1,n2,o1):
    o2 = math.sin(math.radians(o1))*n1/n2
    if (o2 < 1):
        return False
    else:
        return True