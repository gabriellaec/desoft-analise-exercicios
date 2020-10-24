import math
def reflexao_total_interna(n1,n2,o1):
    sin_o2=(n1*meth.sin(math.radians(o1)))/n2
    if sin_o2>1:
        return True
    else:
        return False