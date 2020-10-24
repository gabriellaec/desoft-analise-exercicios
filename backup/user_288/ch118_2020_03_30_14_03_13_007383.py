import math
def reflexao_total_interna (n1, n2, θ2):
	θ1 = math.degrees(math.asin(math.sin(math.radians (θ2)) * n1 / n2))
	if math.sin == 0 and math.sin <= 90:
		reflexao_total_interna = True
		print ('Reflexão Interna')
	else:
		reflexao_total_interna = False
		print ('Refração')