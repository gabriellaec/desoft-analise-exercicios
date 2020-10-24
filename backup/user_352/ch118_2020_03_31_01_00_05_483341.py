import math
def reflexao_total_interna(n1, n2, teta2):
    z=math.radians(teta2)
    x=math.sin(z)
    sin_teta1=(x*n2)/n1
    if sin_teta1<x:
        return False     
    else:
        return True
        
   
    
    