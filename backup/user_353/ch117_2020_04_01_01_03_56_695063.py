import math
def snell_descartes(n1,n2,a1):
    a2=math.degrees((n1*math.sin(math.radians(a1)))/n2)
	print(a2)