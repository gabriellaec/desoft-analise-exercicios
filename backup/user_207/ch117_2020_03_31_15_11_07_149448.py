from math import sin, asin, pi, sqrt
n1 = 1.0
n2 = 1.0
theta01 = 30 #valor em GRAUS


def snell_descartes (n1,n2,theta01):
    seno_theta02 = n1/n2 * sin(theta01/360 *2*pi)
    return asin(seno_theta02)*180/pi

print (snell_descartes(1.0, 1/sqrt(3), 30))