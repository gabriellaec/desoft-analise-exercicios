import math
def reflexao_total_interna(o2,n1,n2):
    o1=math.sin(o2*math.pi/180)*n2/n1
    a=math.sin(o1)
    if a > 1:
        return True
    else:
        return False
