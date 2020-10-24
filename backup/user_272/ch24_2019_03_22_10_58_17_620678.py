def classifica_triangulo(a,b,c):
    if a==b and a==b and c==a:
        return 'equilátero'
	elif a!=b and a!=c and b!=c:
        return 'escaleno'
    else:
        return 'isósceles' 
print(classifica_triangulo(a,b,c))