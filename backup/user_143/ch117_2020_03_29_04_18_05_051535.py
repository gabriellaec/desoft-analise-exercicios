import math
def snell_descartes(n1, n2, o):
    y=(n1/n2)
    x=math.sin(math.radians(o))
    z=x*y
    o2= math.asin(math.radians(z))*57.2958
    return o2