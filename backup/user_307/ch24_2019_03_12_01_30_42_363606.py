a=5
b=7
c=8

def classifica_triangulo(a,b,c):
	if a!=b!=c!=a:
		return 'escaleno'
	elif a==b and b!=c or a==c and c!=b or b==c and c!=a:
		return 'isósceles'
	else:
		return 'equilátero'
print(classifica_triangulo(a,b,c))
