import math
def snell_descartes(n1,n2,t1) :
    t = math.radians(t1)
    t2 = math.asin(n1 + math.sin(t)/n2)
    t2 = math.degrees(t2)
    return t2
    
    
