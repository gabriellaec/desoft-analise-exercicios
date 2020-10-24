import math
def snell_descartes(n1, n2, o):
    y=(n1/n2)
    x=math.sin(o)
    z=x*y
    o2= math.asin(math.degrees(z))
    return o2