import math
def reflexao_total_interna(n1,n2,o2):
    o1=(math.sin(math.radians(o2)*n1))/n2
    if o1 > 1:
    print(o1)
        return True
    else:
        return False