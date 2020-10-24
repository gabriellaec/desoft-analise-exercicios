import math
def reflexao_total_interna(n1,n2,o2):
    y=n1/(n2*math.sin(math.radians(o2)))
    if y > 1:
        return True
    else:
        return False
   
    
   
