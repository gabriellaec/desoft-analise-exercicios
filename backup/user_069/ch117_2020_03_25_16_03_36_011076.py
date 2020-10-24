import math
def snell_descartes (n1,n2,theta1):
    x = n1*math.sin(math.radians(theta1))/n2
    y = math.asin(x)
    theta = math.degrees(y)
    return theta2