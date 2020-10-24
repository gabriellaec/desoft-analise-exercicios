import math
def snell_descartes(n1,n2,teta1):
    a = (n1/n2)*math.sin(math.radians(teta1))
    teta2 = math.degrees(asin(a))
    return teta2
    
