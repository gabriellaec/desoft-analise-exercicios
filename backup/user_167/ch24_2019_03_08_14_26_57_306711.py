def classifica_triangulo(x,y,z):
	if   x==y and x==z:
	     return "equilátero"
	elif x==z or x==y or y==z:
	     return "isóceles"
	else:
	     return "escaleno"