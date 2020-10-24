import math
def snell_descartes (n1, n2, θ1):
	θ2 = math.degrees(math.asin(math.sin(math.radians (θ1)) * n1 / n2))
	return θ2