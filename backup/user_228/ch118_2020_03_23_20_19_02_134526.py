import math
def snell_descartes(n1,n2,s):
    a=n1*math.sin(math.radians(s))/n2
    y=math.asin(a)
    return(math.degrees(y))
    