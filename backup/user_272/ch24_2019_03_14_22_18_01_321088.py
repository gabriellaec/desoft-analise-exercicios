def classifica_triangulo(a,b,c):
    if a==b and a==b and c==a:
        return 'equilátero'
	elif a==b and a!=c:
        return 'isósceles'
    else:
        return 'escaleno' 
print(classifica_triangulo(a,b,c))