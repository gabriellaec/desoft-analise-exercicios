import math
def reflexao_total_interna (n1, n2, a2):
     a1 = math.radians(math.asin ((n2*math.sin(math.radians(a2))/n1)))
    if (n2*math.sin(math.radians(a2))/n1) >= 1:
        return True
    else:
        return False
    return a1
    