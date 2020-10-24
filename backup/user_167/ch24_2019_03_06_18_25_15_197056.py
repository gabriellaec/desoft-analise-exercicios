def classifica_triangulo(x,y,z):
	if x==y and x==z and y==z:
	     print("triângulo equilatero")
	elif x==z or x==y or y==z:
	     print("triângulo isóceles")
	else:
	     print("triângulo escaleno")