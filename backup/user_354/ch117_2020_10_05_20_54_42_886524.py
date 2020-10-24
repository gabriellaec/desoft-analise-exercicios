import math
def snell_descartes(n1,n2,o1):
    
    
    y=(math.sin(math.radians(o1))*n1)/n2
    a=math.asin(y)
    
    return  a
    