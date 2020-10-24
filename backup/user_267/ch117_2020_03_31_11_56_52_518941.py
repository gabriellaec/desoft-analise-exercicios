from math import sin
def snell_descartes(n1,n2,teta1):
	teta2=math.degrees((n1/n2)*(math.asin(sin(teta1))))
	return teta2
    