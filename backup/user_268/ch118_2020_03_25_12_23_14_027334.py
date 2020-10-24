import math
def reflexao_total_interna(n1,n2,o2):
    r2= o2*math.pi/180
    v= math.sin(n2*math.sin(r2)/n1)
    if v>1:
        return True
    else:
        return False