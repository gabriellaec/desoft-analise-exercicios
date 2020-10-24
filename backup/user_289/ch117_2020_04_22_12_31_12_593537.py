import math
def snell_descartes(n1, n2, theta1):
    return math.degrees(math.asin(n1/n2*math.sin(math.radians(theta1)))) 
 