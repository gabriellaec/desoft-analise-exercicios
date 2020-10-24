import math
def snell_descartes(n1,n2,o1):
    x =math.sin(math.radians(o1))*n1/n2
    # x = seno de o2
    y= math.asin(x)
    o2r= math.degrees(y)
    return (o2r)