import math
def snell_descartes(n1,n2,x):
    xr=math.radians(x)
    y= math.asin((math.sin(xr)*n1)/n2)
    yr=math.degrees(y)
    return yr