import math
def snell_descartes(n1,n2,theta1):
    x = (math.sin(theta1)*n1)/n2
    y = math.asin(x)
    theta2 = math.degrees(y)
    return theta2