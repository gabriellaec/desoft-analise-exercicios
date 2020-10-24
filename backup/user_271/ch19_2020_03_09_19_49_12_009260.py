def classifica_triangulo (a,b,c):
	if a==b and a==c:
		print 'equilátero'
	elif a==b or b==c or c==a:
		print 'isóceles'
	else:
		print 'escaleno'
    
a=float(input('o primeiro lado é: '))
b=float(input('o segundo lado é: '))
c=float(input('o terceiro lado é: '))