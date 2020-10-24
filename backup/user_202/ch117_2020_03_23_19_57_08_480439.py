import math
def  snell_descartes(n1,n2,o1):
    o1 = math.radians(o1)
    x = (n1*math.sin(o1))/n2
    x = math.sin(x)
    o2 = math.asin(x)
    o2 = math.degrees(o2)
    return(o2)