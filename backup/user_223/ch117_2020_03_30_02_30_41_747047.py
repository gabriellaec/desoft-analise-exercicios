import math
def snell_descartes (n1,n2,teta1): #n é o índice de refração do meio
	teta2 = (n1/n2)*math.sin(teta1)
	return math.sin(math.asin(teta2))