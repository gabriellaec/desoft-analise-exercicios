import math
def reflexao_total_interna (n1,n2,ang2):
    seno1=(n2*math.sin(math.radians(ang2)))/n1
    if seno1>1:
        return True
    else:
        return False