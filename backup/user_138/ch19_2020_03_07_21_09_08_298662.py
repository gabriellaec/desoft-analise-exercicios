def classifica_triangulo (x,y,z):
    if x==y==z:
        return 'equilátero'
	elif x==y and y!=z:
        return 'isóceles'
	else:
        return 'escaleno'
