import math
def snell_descartes(n1, n2, o):
    o2=0
    y=(n1/n2)
    x=math.sin(math.degrees(o))
    z=math.sin(math.degrees(o2))
    z=x*y
    o2= math.arcsin(z)
    return o2