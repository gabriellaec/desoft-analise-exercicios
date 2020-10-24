import math
def snell_descartes(n1, n2, a1):
    y = math.sin(a1)
    a2 = (math.degrees(y)*n1)/n2 
    return a2
    
    