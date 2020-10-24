def classifica_triangulo(a,b,c):
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))
    if a == b:
        if b == c:
            return 'equilátero'
        elif b != c:
            return isóceles
        else:
            return 'escaleno'
    
    	