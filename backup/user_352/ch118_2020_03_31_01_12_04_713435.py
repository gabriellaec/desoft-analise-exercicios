import math
def reflexao_total_interna(n1, n2, teta2):
    z=math.radians(teta2)
    x=math.sin(z)
    teta1=(x*n2)/n1
    if teta1>=1:
        return True     
    else:
        return False
        
   
    
    