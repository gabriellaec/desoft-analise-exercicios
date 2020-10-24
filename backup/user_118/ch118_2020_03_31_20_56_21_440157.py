import math
def reflexao_total_interna(n2,teta2,n1):
    teta1=math.sin((n2*math.sin(math.radians(teta2)))/n1)
    return teta1
    if teta1>teta2:
        return True
    else:
        return False
    