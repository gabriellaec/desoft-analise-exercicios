import math
def reflexao_total_interna(n1, n2, teta2):
    z=math.radians(teta2)
    x=math.sin(z)
    sin_teta1=(x*n2)/n1
    y=math.asin(sin_teta1)
    teta1=math.degrees(y)
    if teta1>=x:
        return True     
    else:
        return False
        
   
    
    