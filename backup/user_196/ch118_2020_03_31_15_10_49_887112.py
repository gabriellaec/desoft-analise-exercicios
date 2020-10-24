import math
def reflexao_total_interna(n1, n2, ang2):
    a = (n2* math.sin(ang2)) / n1
    if a > 1:
        return True
    else:
        return False
    