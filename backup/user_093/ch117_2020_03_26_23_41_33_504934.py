import math
def snell_descartes(n1,n2,x):
    y=(n1/n2)*(math.asin(x))
    z=math.radians(y)
    return z
