import math

def snell_descartes(n1, n2, teta1)
	y = math.pi*math.asin((n1/n2)*math.sin(teta1*math.pi/180))/180
    return y