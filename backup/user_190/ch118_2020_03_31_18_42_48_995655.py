import math
def reflexao_total_interna(n1, n2, o2):
    L=n1/n2
    o1=math.asin(math.degrees(L))
    if o1>o2:
        return True
    else: 
        return False