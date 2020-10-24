import math
def snell_descartes(n1,n2,t1) :
    t1 = math.radians(t1)
    t2 = math.asin((n1*math.sin(t1))/n2)
    t2 = degrees(t2)
    return t2
    
    
