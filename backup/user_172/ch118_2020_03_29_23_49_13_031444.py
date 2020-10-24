import math
def reflexao_total_interna (n1, n2, o2):
    sen_l = n2*(math.sin(math.radians(o2)))/n1
    if sen_l>1:
        return True
    else:
        return False
        