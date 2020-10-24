import math
def snell_descartes(n1,n2,teta1):
    x = math.sin(math.radians(teta1))
    z =(n1*x)/n2
    teta2 = math.asin(z)
    return math.degrees(teta2)