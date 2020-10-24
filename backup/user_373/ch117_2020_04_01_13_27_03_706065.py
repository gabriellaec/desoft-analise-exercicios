import math
def snell_descartes (n1,n2,o1):
    y = (n1/n2) * math.sin(math.radians(o1)) 
    x= math.asin(y)
    return math.degrees(x)
    
    
