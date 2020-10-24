import math
def reflexao_total_interna (n1, n2, o2):
    sin_l = n1*(math.sin(math.radians(o2)))/n2
    if sin_l>1:
        return True
    else:
        return False
        