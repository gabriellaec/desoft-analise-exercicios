def classifica_triangulo(x, y, z):
    if x == y and x == z:
    	return "equilátero"
    elif (x == y and y != z) or (y == z and z != x) or (x == z and z != y):
        return "isósceles"
    else:
    	return "escaleno"