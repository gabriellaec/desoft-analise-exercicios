import math
def snell_descartes(n1, n2, theta1):
    t2 = n1*(math.sin(math.radians(theta1)))/n2
    theta2 = math.degrees(math.asin(t2))
    return theta2