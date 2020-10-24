import math
def snell_descartes(n1,n2,teta1):
	teta2=math.degrees((n1/n2)*(math.asin(math.sin(teta1))))
	return teta2
    