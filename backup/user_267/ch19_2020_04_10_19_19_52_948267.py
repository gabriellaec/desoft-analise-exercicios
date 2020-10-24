def classifica_triangulo(x, y, z):
    if x == y and x == z:
    	print("equilátero")
    elif (x == y and y != z) or (z == y and y != x) or (x == z and z != y):
        print("isósceles")
    else:
    	print("escaleno")