import math
def reflexao_total_interna(n1,n2,i1):
    i1 = math.radians(i1)
    i2 = n2*(math.sin(i1))/n1
    if i2 > 1:
        return True
    else:
        return False