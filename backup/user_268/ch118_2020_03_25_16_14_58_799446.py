import math
def reflexao_total_interna(n1,n2,o2):
    r2=math.radians(o2)
    n=(n1*math.sin(r2)/n2)
    if n>1:
        return True
    else:
        return False