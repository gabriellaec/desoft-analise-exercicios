import math
def reflexao_total_interna(n1, n2, teta2):
	teta1 = (n2/n1)*math.sin(math.radians(teta2))
    teta1_asin = math.asin(teta1)
    if math.degrees(teta1_asin)>1:
		return (True)
	else:
		return (False)