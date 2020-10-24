import math
def reflexao_total_interna(n1, n2, a2):
    a2 = a2 * (math.pi/180)
    a1 = math.asin((math.sin(a2))*n2/n1)
    if math.sin(a2) > 1:
        return True
    else:
        return False
    