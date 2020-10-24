import math

def reflexao_total_interna(n1, n2, a2):
    a2 = math.radians(a2)
    a1 = (math.sin(a2)*n2)/n1
    x = math.sin(a1)
    if x>1:
        return True
    else:
        return False