def classifica_triangulo(x,y,z):
	if   x==y or x==z or z==y:
	     return "triângulo equilatero"
	elif x==z or x==y or y==z:
	     return "triângulo isóceles"
	else:
	     return "triângulo escaleno"