import math
def snell_descartes (n1, n2, teta1):
    y=(n1*math.sin(math.radians(teta1)))/n2
    x=math.asin(y)
    teta2=math.degrees(x)
    return teta2