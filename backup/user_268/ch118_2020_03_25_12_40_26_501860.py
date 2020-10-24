import math
def reflexao_total_interna(n1,n2,o2):
    r2=(o2*math.pi)/180
    n=math.sin(n1*math.sin(r1)/n2)
    if n>1:
        return True
    else:
        return False