import math
def snell_descartes(n1, n2, a1):
    y = math.sin(a1)
    x = (y*180)/math.pi
    a2 = (x*n1)/n2 
    return a2
    
    