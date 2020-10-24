import math
def reflexao_total_interna(n1,n2,t2):
    st1 = n2 * math.sin(math.degrees(t2))/n1
    if st1 > 1:
        return True
    else:
        return False
    