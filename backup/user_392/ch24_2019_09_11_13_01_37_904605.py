def classifica_triangulo(a,b,c):
	if a==b and a==c:
        return 'equilátero'
    elif a==b and b==c and a!=c or a==c and b==c and b!=a:
        return 'isósceles'
    else:
		return 'escaleno'
    