import math
def snell_descartes(n1, n2, teta1):
    math.radians(teta1)
    sin_teta2=n1*math.sin(teta1)/n2
    teta2=math.asin(sin_teta2)
    math.degrees(teta2)
    return teta2

