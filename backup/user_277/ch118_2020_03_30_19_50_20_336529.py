import math
def reflexao_total_interna(n1,n2,o2):
    o1=math.asin(n2*math.sin(o2)/n1)
    if math.sin(o1)>1:
        return True
    else:
        return False
