import math
def reflexao_total_interna(n1,n2,O2):
    O = math.radians(O2)
    a = math.sin(O)
    c = (n2/n1)*a
    if c > 1:
        return True
    else:
        return False