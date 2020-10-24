def classifica_triangulo(a, b, c):
    a = input('a: ')
    b = input('b: ')
    c = input('c: ')
    if a == b and a == c:
            return 'equilátero'
	elif a != b and a != c and b != c:
        return 'isóceles'
    else:
        return 'escaleno'