def classifica_triangulo(x,y,z):
	if x==y and x==z and y==z:
	     return("triângulo equilatero")
	elif x==z or x==y or y==z:
	     return("triângulo isóceles")
	else:
	     return("triângulo escaleno")