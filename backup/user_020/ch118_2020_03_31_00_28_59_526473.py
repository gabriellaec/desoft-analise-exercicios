import math
def reflexao_total_interna(n1,n2,teta2):
    teta2 = math.radians(teta2)
    o1 = n2*math.sin(o2)/n1
    if o1 > 1:
        return True
    else:
        return False
print(reflexao_total_interna(1,2,-90))