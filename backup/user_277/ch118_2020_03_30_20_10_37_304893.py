import math
def reflexao_total_interna(n1,n2,o2):
    o2=(n1/n2)*math.sin(o1*math.pi/180)
    a=math.sin(o2)
    if a > 1:
        return True
    else:
        return False
