import math
def reflexao_total_interna(n1, n2, teta2):
	seno_teta1 = (n2/n1)*math.sin(math.radians(teta2))
	if math.desgrees(seno_teta1)>1:
		return (True)
	else:
		return (False)