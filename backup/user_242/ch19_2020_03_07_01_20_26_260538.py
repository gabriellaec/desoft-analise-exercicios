def classifica_triangulo (X,Y,Z):
    if X == Y == Z:
        return 'Equilátero'
    elif X != Y != Z:
        return 'Escaleno'
    else:
        return 'Isoceles'

print(classifica_triangulo(5,5,7))
