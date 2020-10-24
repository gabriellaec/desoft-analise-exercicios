import math

def snell_descartes(n1,n2,teta1):
    y = n1/n2
    x = math.asin(math.radians(teta1))
    z = y*x
    teta2 = math.asin(z)
    return math.degrees(teta2)