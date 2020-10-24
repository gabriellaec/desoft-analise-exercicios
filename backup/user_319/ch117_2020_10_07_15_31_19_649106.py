import math
def snell_descartes(n1,n2,teta_1):
    y= math.degrees(math.asin((n1*math.sin(math.radians(teta_1))/n2)))   
    return y
