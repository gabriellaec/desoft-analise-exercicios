import math
def snell_descartes (n1,n2,theta1):
    x = n1/n2*math.sin(math.radians(theta1))
    y = math.asin(x)
    theta2 = math.degrees(y)
    return theta2