import math
def snell_descartes(n1, n2, teta2):
    z=math.radians(teta2)
    x=math.sin(z)
    sin_teta1=(x*n2)/n1
    if sin_teta1<x:
        return falso     
    else sin_teta2>=x:
        return verdadeiro
        
   
    
    