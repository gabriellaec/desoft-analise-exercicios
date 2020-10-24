import math
def reflexao_total_interna(n1,n2,a2):
    sin_a1=(n2*math.sin(math.radians(a2)))/n1
    if sin_a1>1:
        return True 
    else:
        return False