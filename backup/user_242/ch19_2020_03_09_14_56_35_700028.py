def classifica_triangulo (X,Y,Z):
    if not (X+Y) > Z and (X+Z) > Y and (Z+Y) > X:
        return 'Isso não é um triâgulo'
    elif X != Y and X != Z and Y != Z:
        return 'Escaleno'
    elif X == Y and X == Z and Y==Z:
        return 'Equilátero'
    else:
        return 'Isósceles'

print (classifica_triangulo(1,1,2))