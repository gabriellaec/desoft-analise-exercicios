def classifica_triangulo(x,y,z):
	if x==y==z:
		return "equilátero"
	if x==y or x==z or z==y:
		return "isósceles"
	else:
		return "escaleno"