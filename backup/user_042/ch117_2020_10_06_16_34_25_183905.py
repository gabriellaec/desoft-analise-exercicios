import math
def snell_descartes(n1, n2, a1):
    y = math.sin(a1)
    a2 = (n1/n2)*y 
    return a2
    
    