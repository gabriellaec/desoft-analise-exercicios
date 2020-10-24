import math
def reflexao_total_interna(n1, n2, O2):
    refle=(n2*math.sin(math.radians(O2)))/n1
    if refle>1:
        return True
    else:
        return False
        