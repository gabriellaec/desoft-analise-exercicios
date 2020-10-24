import math

def reflexao_total_interna(n1, n2, θ2,):
    return math.degrees(math.asin((n2*math.sin(math.radians(θ2))/n1))) > 90
	
    