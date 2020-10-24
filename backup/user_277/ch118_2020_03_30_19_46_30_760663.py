import math
def reflexao_total_interna(n1,n2,o2):
    o1=math.asin(((math.sin(o2*math.pi/180)*n1)/n2))
    if math.sin>1:
        return True
    else:
        return False
