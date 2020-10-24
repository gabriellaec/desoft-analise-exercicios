import math

def snell_descartes (n1, n2, theta1_ang):
    theta1_rad = theta1_ang*math.pi/180
    theta2_rad = math.sin(math.sin(theta1_rad)*n1/n2)
    theta2_ang = 180*theta2_rad/math.pi

    return theta2_ang