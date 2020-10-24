def   classifica_triangulo(x,y,z):
    if x == y == z:
        return 'equilatero'
    else:
        if x == y != z:
            return 'Isoceles'
        else:
            return 'Escaleno'
print(classifica_triangulo(30,30,30))
print(classifica_triangulo(90,45,15))