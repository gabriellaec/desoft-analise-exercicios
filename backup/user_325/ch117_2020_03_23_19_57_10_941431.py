import math
def snell_descartes(n1,n2,o1):
    a = math.sin(o1)
    b = math.degrees(a)
    c = (n1/n2) * b
    d = math.asin(c)
    return d
    
    
    