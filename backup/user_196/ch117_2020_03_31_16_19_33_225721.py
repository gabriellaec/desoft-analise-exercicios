import math
def snell_descartes(n1,n2,ang1): 
    ang2 = (n1 * (math.sin(ang1))) / n2
    return math.asin(ang2)