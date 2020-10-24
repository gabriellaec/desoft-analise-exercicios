import math
def snell_descartes(n1, n2, teta1):
    math.radians(teta1)
    x=n1*math.sin(teta1)/n2
    teta2=math.asin(x)
    math.degrees(teta2)=teta2
    return teta2

