import math
def snell_descartes(n1, n2, a1):
    a= math.sin(math.radians(a1))
    a2 = (n1/n2)*math.degrees(a) 
    return a2
    
    