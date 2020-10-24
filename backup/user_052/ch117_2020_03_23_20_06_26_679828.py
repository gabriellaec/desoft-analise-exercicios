import math
def snell_descartes (n1,n2,o1):
	x = n2 / math.sin(math.radians(o1)) * n1
	y = math.asin(x)
	return math.degrees(y)