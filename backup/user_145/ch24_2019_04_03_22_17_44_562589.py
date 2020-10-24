def classifica_triangulo(a,b,c):
    if a == b and b == c:
        return 'equilatero'
	if a == b and b != c:
        return 'isocelis'
	else:
        return 'escaleno'
