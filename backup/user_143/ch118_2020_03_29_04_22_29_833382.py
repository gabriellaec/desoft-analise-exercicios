import math
def snell_descartes(n1, n2, o):
    y=(n1/n2)
    x=math.sin(math.radians(o))
    z=x*y
    o2= math.asin(z)
    o2=math.degrees(o2)
    return o2
def reflexao_total_interna (n1, n2, o2):
    if 