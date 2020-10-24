import math

def reflexao_total_interna(n1,n2,o2):
    sin = n2 *math.sin(math.radians(o2))/n1
    if sin >1.00:
        return True
    else:
        return False