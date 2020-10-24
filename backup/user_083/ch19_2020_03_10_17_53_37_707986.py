def   classifica_triangulo(x,y,z):
    if x == y == z:
        return 'equilátero'
    else:
        if x == y != z:
            return 'isósceles'
        else:
            return 'escaleno'
print(classifica_triangulo(30,30,30))
print(classifica_triangulo(90,45,15))