import math

def snell_descartes(n1,n2,teta1):
	teta2 = (n1/n2)*math.sin(math.radians(teta1))
	x = math.asin(teta2)
	return math.degrees(x)