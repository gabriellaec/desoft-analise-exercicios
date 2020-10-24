import math

def snell_descartes (n1, n2, theta1_ang):

    sin_theta2 = math.sin(math.radians(theta1_ang))*n1/n2
    theta2_rad = math.asin(sin_theta2)
    theta2_ang = math.degrees(theta2_rad)

    return theta2_ang