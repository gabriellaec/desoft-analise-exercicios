def classifica_triangulo(x,y,z):
	if   x==y and x==z:
	     return "equilátero"
	elif x==z or x==y or y==z:
	     return "isósceles"
	else:
	     return "escaleno"