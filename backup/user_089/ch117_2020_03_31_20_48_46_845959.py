import math

def snell_descartes(n1,n2,a):
    b = (n1/n2)*(math.sin(math.radians(a)))
    
    return b