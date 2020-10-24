import math
def reflexao_total_interna(n1,n2,o2):
    o2=math.radians(o2)
    a=(n2/n1)*math.sin(o2)
    #o1 = seno(o1)
    if a> 1:
        return True
    else:
        return False
    