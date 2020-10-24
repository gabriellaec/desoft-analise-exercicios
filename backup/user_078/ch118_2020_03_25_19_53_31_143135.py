import math
def reflexao_total_interna (n1,n2,t2):
    sin_t1=(n2*math.sin(math.radians(t2)))/n1
    if sin_t1>1:
        return True
    else:
        return False