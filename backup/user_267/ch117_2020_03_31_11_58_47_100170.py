from math import sin,asin,degrees
def snell_descartes(n1,n2,teta1):
	teta2=math.asin(math.degrees((n1/n2)*(math.sin(teta1))))
	return teta2
    