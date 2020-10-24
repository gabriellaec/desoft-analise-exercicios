def classifica_triangulo (X,Y,Z):
    if X != Y and X != Z and Y != Z:
        return 'Escaleno'
    elif X == Y and X == Z and Y==Z:
        return 'Equilátero'
    else:
        return 'Isósceles'

print (classifica_triangulo(1,1,2))