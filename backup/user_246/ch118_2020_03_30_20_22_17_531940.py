import math
def reflexao_total_interna(n1, n2, o2):
    o2=math.radians(o2)
    o1=n2*o2/n1
    if o1>1:
        return True
    else:
        return False
    
    