import math

def reflexao_total_interna(n1, n2, T2):
    
    x = ((math.sin(T2))*n2)/n1
    
    if x > 1:
        return True
    
    else:
        return False