def classifica_triangulo(x, y, z):
    if (x == y and x != z) or (x == z and x != y) or (y == z and y !=x):
		return("isósceles")
	elif y != x and x != z and y != z :
		return("escaleno")
	else:
		return("equilátero")
print(classifica_triangulo(3, 1, 3))