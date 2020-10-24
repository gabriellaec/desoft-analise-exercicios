import math
def reflexao_total_interna(n1,n2,o2):
    o1=(1/n1)**n2math.sin(o2*math.pi/180)
    a=math.sin(o1)
    if a > 1:
        return True
    else:
        return False
