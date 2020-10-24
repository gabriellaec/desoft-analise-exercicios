import math 

def reflexao_total_interna (n1,n2,o2):
    sin_t2 = n2 + math.sin(math.radians(o2)) / n1
    if sin_t2 > 1.0:
        return True 
    else:
        return False 
    