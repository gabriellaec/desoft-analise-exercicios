import math

def snell_descartes (n1,n2,a1):
    x= (math.sin(math.radians(a1)*n1))/n2
    z= math.asin(x)
    return math.degrees(z)