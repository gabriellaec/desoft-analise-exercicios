import math
def snell_descartes (n1,n2,θ2):
	θ1=math.degrees(math.asin(n1*math.sin(math.radians(θ2)))/n2)
	return θ1