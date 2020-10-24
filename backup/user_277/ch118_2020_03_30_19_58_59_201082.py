import math
def reflexao_total_interna(n1,n2,o2):
    o1=n2*math.sin(o2)/n1
    a=math.sin(o1)
    if a > 1:
        return True
    else:
        return False
