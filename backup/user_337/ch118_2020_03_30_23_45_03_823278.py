import math
def reflexao_total_interna(n1, n2, o2):
    x =(n2/n1)*math.sin(math.degrees(o2))
    if x >= 1:
        return True
    else:
        return False