import math
def snell_descartes(n1, n2, teta1):
    math.radians(teta1)
    x=math.sin(teta1)
    sin_teta2=x*n1/n2
    y=math.asin(sin_teta2)
    teta2=math.degrees(y)
    return teta2

