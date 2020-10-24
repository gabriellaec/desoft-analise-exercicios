def classifica_triangulo(a,b,c):
    a = input('a: ')
    b = input('b: ')
    c = input('c: ')
    if a == b:
        if b == c:
            return 'equilátero'
        elif b != c:
            return 'isóceles'
    else:
		return 'escaleno'
    
    	