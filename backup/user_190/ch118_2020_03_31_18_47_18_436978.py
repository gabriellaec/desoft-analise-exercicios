import math
def reflexao_total_interna(n1, n2, o2):
    L=n1/n2
    o1=math.sin(math.radians(L))
    if o2>o1:
        return True
    else: 
        return False