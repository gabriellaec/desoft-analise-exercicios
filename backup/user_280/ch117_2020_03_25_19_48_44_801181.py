import math

def snell_descartes(n1, n2, teta1):
	y = 180*math.asin(n1*math.sin(teta1*math.pi/180)/n2)/math.pi
    return y