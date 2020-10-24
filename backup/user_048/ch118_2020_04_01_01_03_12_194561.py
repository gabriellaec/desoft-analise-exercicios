import math
def reflexao_total_interna(n1,n2,o2):
    o2=math.radians(o2)
    math.sin(o1)=(n2/n2)*math.sin(o2)
    if math.sin(o1)> 1:
        return True
    elif math.sin(o1)==1:
        pass
    else:
        return False
    