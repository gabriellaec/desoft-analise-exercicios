import math
def snell_descartes(n1, n2, O1):
    x=math.sin(math.radians(O1))
    y=(n1*x)/n2
    O2=math.asin(y)
    return math.degrees(O2)
    
