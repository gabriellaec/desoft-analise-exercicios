import math
def snell_descartes(n1,n2,a):
    a=math.radians(a)
    y=math.sin(a)*n1/n2
    y=math.degrees(y)
    return y
    