import math
def snell_descartes(n1,n2,theta1):
    theta2 = n1/n1 * math.sin(math.radians(theta1))
    return theta2
        