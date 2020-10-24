import math
def snell_descartes(n1, n2, O1):
    y=(n1/n2)
    x=math.sin(O1)
    z=x*y
    O2=math.asin(z)
    return math.degrees(O2)
    
