import math

def reflexao_total_interna(n1, n2, T2):
    
    T1 = (math.sin(math.radians(T2))*n2)/n1
    
    if T1 > 1:
        return True
    
    else:
        return False