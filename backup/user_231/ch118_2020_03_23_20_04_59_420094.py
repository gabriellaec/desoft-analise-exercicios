import math
def reflexao_total_interna(n1,n2,o2):
    a= math.radians(o2)
    b= math.sin(a)
    c=n2*b/n1
    if c>1:
        return True
    else:
        return False
        
    
    