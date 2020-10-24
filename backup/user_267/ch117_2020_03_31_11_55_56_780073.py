from math import sin
def snell_descartes(n1,n2,teta1):
	teta2=(n1/n2)*(math.asin(sin(math.degrees(teta1))))
	return teta2
    